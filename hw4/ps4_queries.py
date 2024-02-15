#
# CS 460: Problem Set 4: XQuery Programming Problems
#

#
# For each query, use a text editor to add the appropriate XQuery
# command between the triple quotes provided for that query's variable.
#
# For example, here is how you would include a query that finds
# the names of all movies in the database from 1990.
#
sample = """
    for $m in //movie
    where $m/year = 1990
    return $m/name
"""

#
# 1. Put your query for this problem between the triple quotes found below.
#    Follow the same format as the model query shown above.
#
query1 = """
    for $d in //person[@directed]
    where $d[contains(pob, "Canada")]
    return $d/name
"""

#
# 2. Put your query for this problem between the triple quotes found below.
#
query2 = """
    for $d in //person[@directed]
    where $d[contains(pob, "Canada")]
    order by $d/name
    return <canadian_dir>
        {$d/name/text(), " (",$d/pob/text(), ")"}
    </canadian_dir>
"""

#
# 3. Put your query for this problem between the triple quotes found below.
#
query3 = """
    for $d in //person[@directed and contains(pob, "Canada")]
    let $dm := //movie[contains(@directors, $d/@id)]
    let $avg := avg($dm/runtime)
    let $top := count($dm[earnings_rank])
    order by $d/name
    return <canadian_dir>
        {
            $d/name, $d/pob,
            for $m in distinct-values($dm/name)
            return <directed>{$m}</directed>,
            <avg_runtime>{$avg}</avg_runtime>,
            <num_top_grossers>{$top}</num_top_grossers>
        }
    </canadian_dir>
"""

#
# 4. Put your query for this problem between the triple quotes found below.
#
query4 = """
    for $p in //person, 
    $o1 in //oscar[@person_id = $p/@id],
    $o2 in //oscar[@person_id = $p/@id]
    where $o1/year - $o2/year = -1
    return 
    <back_to_back>{
        <name>{$p/name/text()}</name>,
        <first_win>{$o1/type/text(), " (", $o1/year/text(), ")"}</first_win>,
        <second_win>{$o2/type/text(), " (", $o2/year/text(), ")"}</second_win>
    }</back_to_back>
"""
