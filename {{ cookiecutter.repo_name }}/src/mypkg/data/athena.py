from pyathena import connect


def athena(
    s3_directory="s3://aws-athena-query-results-164810850900-eu-west-1/",
    work_group="MarketingScientist",
):
    """Connect to AWS Athena

    Args:
        s3_directory (str, optional): Defaults to "s3://aws-athena-query-results-164810850900-eu-west-1/".
        work_group (str, optional): Defaults to "MarketingScientist".

    Returns:
        connection:
    """
    try:
        conn = connect(
            s3_staging_dir=s3_directory, region_name="eu-west-1", work_group=work_group
        )
        return conn
    except:
        print("Error: Check aws token bat and re-run!")
