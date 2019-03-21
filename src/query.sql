SELECT law_section_number
    , offense_description
    , borough
    , sex
    , race
    , COUNT(*) AS n
FROM data
WHERE sex IS NULL
AND race IS NULL
GROUP BY law_section_number
    , offense_description
    , borough
    , sex
    , race
ORDER BY COUNT(*) DESC;
