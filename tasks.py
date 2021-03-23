from invoke import task


@task(aliases=["fmt"])
def format(ctx):
    commands = [
        "black ./",
        "isort ./",
        "autoflake -i -r --remove-unused-variables --remove-all-unused-imports ./",
    ]
    for command in commands:
        ctx.run(command)
    print("Done formatting!")


@task
def check(ctx):
    commands = ["black ./ --check", "isort ./ --check-only", "autoflake -c -r ./"]
    for command in commands:
        ctx.run(command)
    print("Done checking!")


@task
def bootstrap(ctx):
    ctx.run("cat requirements.txt | xargs poetry add")
    print("Done bootstrapping!")
