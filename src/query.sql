SELECT offense_description
    , law_section_number
    , COUNT(*) AS n
FROM data
WHERE offense_description = 'ACCEPT ON HAIL'
GROUP BY offense_description
    , law_section_number
ORDER BY COUNT(*) DESC;
