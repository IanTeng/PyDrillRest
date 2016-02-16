# PyDrillRest

Drill Rest CLient For Python

# Example:


<code>import pyDrillRest</code>

<code>drill=pyDrillRest.DrillClient('localhost:8047')</code>

<code>print drill.sqlQuery("SELECT * FROM cp.`employee.json` limit 10")</code>
