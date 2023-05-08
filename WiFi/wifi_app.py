import click
import sys
import the_guts


@click.group()
@click.argument("wireless_interface")
@click.option(
    "-i",
    "--interval",
    type=click.INT,
    default=500,
    help="sampling interval in microseconds",
)
@click.option(
    "-f",
    "--frequency",
    type=click.INT,
    default=5765,
    help="center frequency of the channel to listen on in megahertz",
)
@click.option(
    "-c",
    "--chip_sample_number",
    type=click.INT,
    default=1,
    help="number of samples per chip",
)
@click.pass_context
def cli(ctx, wireless_interface, interval, frequency, chip_sample_number):
    ctx.ensure_object(dict)
    ctx.obj["guts"] = the_guts.Guts(
        wireless_interface, interval, frequency, chip_sample_number
    )


@cli.command(help="actively search and decode babel signal")
@click.option(
    "-m",
    "--method",
    type=click.Choice(["auto_correlation", "interval","std_auto"]),
    default="auto_correlation",
)
@click.option(
    "-s",
    "--switch",
    is_flag=True
)
@click.option(
    "-c",
    "--count",
    is_flag=True
)
@click.pass_context
def active(ctx, method,switch, count):
    guts = ctx.obj["guts"]
    guts.active_decode(method, switch, count)


@cli.command(help="collect samples and write them to file to be processed later")
@click.pass_context
@click.option(
    "-t",
    "--sample_time",
    type=click.INT,
    default=10,
    help="total number of seconds to sample for",
)
@click.option(
    "-o",
    "--output_file",
    type=click.STRING,
    default="/tmp/wifi_channel_measurements.bin",
    help="If writing a info to a file, where to write it",
)
def passive_collection(ctx, sample_time, output_file):
    guts = ctx.obj["guts"]
    guts.passive_capture(sample_time, output_file)


@cli.command(
    help="decode a passively collected sample file, state what symbols are found"
)
@click.pass_context
@click.option(
    "-s",
    "--sample_file",
    type=click.STRING,
    default="/tmp/wifi_channel_measurements.bin",
    help="location of the sample file",
)
@click.option(
    "-m", "method", type=click.Choice(["auto_correlation", "interval","std_auto"]), default="auto_correlation"
)
@click.option(
    "-c",
    "--count",
    is_flag=True
)
@click.option("-g", "--graph", is_flag=True)
def passive_collection_decode(ctx, sample_file, method, graph, count):
    guts = ctx.obj["guts"]
    guts.pass_decode(sample_file, method, graph, count)


if __name__ == "__main__":
    cli(obj={})
