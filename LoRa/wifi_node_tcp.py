import click
import tcp_backend



@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["backend"] = tcp_backend.TCP()

@cli.command(help="create tcp server")
@click.option(
    "-p",
    "--port",
    type=click.INT,
    default=5000,
)
@click.option(
    "-i",
    "--ip_address",
    type=click.STRING,
    default="localhost"
)
@click.pass_context
def server(ctx, port,ip_address):
    TCP = ctx.obj["backend"]
    TCP.server(port,ip_address)

@cli.command(help="create tcp client")
@click.option(
    "-p",
    "--port",
    type=click.INT,
    default=5000,
)
@click.option(
    "-i",
    "--ip_address",
    type=click.STRING,
    default="localhost"
)
@click.option(
    "-r",
    "--rate",
    type=click.FLOAT,
    default=0.5
)
@click.option(
    "-s",
    "--packet_size",
    type=click.INT,
    default= 50
)
@click.pass_context
def client(ctx, port, ip_address, rate, packet_size):
    TCP = ctx.obj["backend"]
    TCP.client(port,ip_address,rate, packet_size)

if __name__ == "__main__":
    cli(obj={})
