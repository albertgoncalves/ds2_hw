SELECT law_section_number
    , offense_description
    , jurisdiction_code
    , borough
    , sex
    , race
    , COUNT(*) AS n
FROM data
GROUP BY law_section_number
    , offense_description
    , jurisdiction_code
    , borough
    , sex
    , race
ORDER BY COUNT(*) DESC;
