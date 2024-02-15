query1 = """
    for $c in //account
    where $c[balance > 400]
    return $c/@account_num
"""

query2 = """
    for $c in //customer
    order by $c/@customer_num
    return <cust_acct>
        <customer>{$c/name/text()}</customer>
        <account>{$c/@customer_num}</account>
    </cust_acct>

"""

query3 = """
    for $c in // customer
    return <customer>
    <name>{$c/name/text()}</name>
    for $a in //account[@owners = $c/@customer_num]
    return <account>{$a/branch/text() ($$a/balance)}</account>
    </customer>
"""