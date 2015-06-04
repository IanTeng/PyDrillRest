# PyDrillRest

Drill Rest CLient For Python

<code>
import pyDrillRest

drill=pyDrillRest.DrillClient('localhost:8047')
print drill.sqlQuery("SELECT * FROM cp.`employee.json` limit 10")
</code>
