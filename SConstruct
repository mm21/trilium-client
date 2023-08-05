import os
import subprocess
import shutil

PROJECT = "trilium-client"
PACKAGE = "trilium_client"
GIT_USER_ID = "mm21"
GIT_REPO_ID = PROJECT
BUILD_DIR = f"build/{PROJECT}"

env = Environment()

# set build artifact dir
build = env.Dir(f"{BUILD_DIR}")


# return list of dependencies in terms of (name, version) given path to
# requirements.txt
def get_dependencies(path_requirements: str) -> list[tuple[str, str]]:
    deps = []

    with open(path_requirements) as fh:
        requirements = fh.read().strip().split("\n")

        for req in requirements:
            req_split = req.strip().split()

            # extract name and version
            name = req_split[0]
            ver = "".join(req_split[1:])

            # skip setuptools - we'll use poetry's packaging
            if name == "setuptools":
                continue

            deps.append((name, ver))

    return deps


# adjust dependencies in place
def tune_dependencies(deps: list[str]):
    for i, (name, ver) in enumerate(deps):
        # pin pydantic version to avoid deprecation warnings
        if name == "pydantic":
            deps[i] = (name, f"{ver} <2")


def build_client(target, source, env):
    path_generator = shutil.which("openapi-generator-cli")

    assert (
        path_generator is not None
    ), "openapi-generator-cli not found, install it from: openapi-generator.tech"

    args = [
        path_generator,
        "generate",
        "-o",
        str(target[0]),
        "-i",
        str(source[0]),
        "-g",
        "python-nextgen",
        "--additional-properties",
        f"projectName={PROJECT}",
        "--additional-properties",
        f"packageName={PACKAGE}",
    ]

    cmd = " ".join(args)
    env["client_cmd"] = cmd

    print(f"Building client with command: {cmd}")

    subprocess.check_call(args)

    # format generated code
    print(f"Formatting code")
    subprocess.check_call(["black", f"{BUILD_DIR}/{PACKAGE}"])

    # install dependencies
    print(f"Installing dependencies")
    dependencies = get_dependencies(f"{BUILD_DIR}/requirements.txt")

    tune_dependencies(dependencies)

    for name, ver in dependencies:
        subprocess.check_call(["poetry", "add", f"{name}@{ver}"])


def build_readme(target, source, env):
    client_readme = f"{str(source[0])}/README.md"

    # read base readme
    with open("README.base.md") as fh:
        base_readme_text = fh.read()

    # read generated readme
    with open(client_readme) as fh:
        client_readme_text = fh.read()

    # substitute strings
    client_readme_text = client_readme_text.replace(
        "GIT_USER_ID", GIT_USER_ID
    ).replace("GIT_REPO_ID", GIT_REPO_ID)

    readme_text = f"{base_readme_text}\n{client_readme_text}"

    with open(str(target[0]), "w") as fh:
        fh.write(readme_text)


def install(target, source, env):
    if os.path.isfile(str(source[0])):
        shutil.copyfile(str(source[0]), str(target[0]))
    else:
        shutil.copytree(str(source[0]), str(target[0]), dirs_exist_ok=True)


# generate readme
readme = env.Command("README.md", build, build_readme)

# get generated artifacts to install
artifacts = [
    env.Dir(f"{BUILD_DIR}/docs"),
    env.Dir(f"{BUILD_DIR}/trilium_client"),
]

etapi_yaml = env.File("etapi.openapi.yaml")
client = env.Command(build, etapi_yaml, build_client)


install_artifacts = [
    env.Command(os.path.basename(str(a)), a, install) for a in artifacts
] + [readme]

env.Default(client, install_artifacts)
env.Clean(client, [build] + install_artifacts)

# also remove poetry dependencies
if GetOption("clean"):
    output = (
        subprocess.check_output(["poetry", "show", "--without=dev", "--tree"])
        .decode()
        .strip()
        .split("\n")
    )

    packages = [
        line.split()[0]
        for line in output
        if len(line) > 0 and line[0].isalnum()
    ]

    if len(packages) > 0:
        subprocess.check_call(["poetry", "remove"] + packages)
