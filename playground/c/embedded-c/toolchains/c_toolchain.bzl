CCompilerInfo = provider(
    fields = ["command"],
)

def _c_toolchain_impl(ctx):
    return [
        DefaultInfo(),
        CCompilerInfo(command = ctx.attrs.command),
    ]

c_toolchain = rule(
    impl = _c_toolchain_impl,
    is_toolchain_rule = True,
    attrs = {
        "command": attrs.string(),
    },
)
