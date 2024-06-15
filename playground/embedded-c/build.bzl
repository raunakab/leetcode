load("@toolchains//c_toolchain.bzl", "CCompilerInfo")

def compile_c_binary_command(ctx, out):
    return cmd_args([
        ctx.attrs.toolchain[CCompilerInfo].command,
        ctx.attrs.file,
        "-o",
        out.as_output(),
    ])


def run_c_binary_command(out):
    return cmd_args([out])


def _c_binary_impl(ctx):
    out = ctx.actions.declare_output("main")

    compile_cmd = compile_c_binary_command(ctx, out)
    ctx.actions.run(compile_cmd, category = "compile")
    run_cmd = run_c_binary_command(out)

    return [
        DefaultInfo(default_output = out),
        RunInfo(args = run_cmd),
    ]


c_binary = rule(
    impl = _c_binary_impl,
    attrs = {
        "file": attrs.source(),
        "toolchain": attrs.toolchain_dep(),
    },
)
