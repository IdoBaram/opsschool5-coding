import click


@click.group()
@click.option('--tags', '-t', type=str, help='Query resources by tags')
@click.option('--cloud', '-c', type=click.Choice(['aws', 'gcp', 'azure'],
                                                 case_sensitive=False), help='Cloud provider to '
                                                                             'query  [default: aws]', default='aws')
@click.pass_context
def cloudctl(ctx, *args, **kwargs):
    """ Cloud Manager cli """


@cloudctl.group()
@click.pass_context
def get(ctx):
    """ get action """
    print(ctx)


@get.group()
@click.pass_context
def instances(ctx):
    """ get instances """
    print(ctx)


@cloudctl.group()
@click.pass_context
def stop(ctx):
    """ stop action """
    print(ctx)


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()
