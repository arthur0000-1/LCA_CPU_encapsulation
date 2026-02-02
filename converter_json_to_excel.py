import json
import pandas as pd

# Load the JSON array
with open('cpuTechPowerUp.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame directly
df = pd.DataFrame(data)

# Export to Excel
df.to_excel('TechPowerUp_cpu.xlsx', index=False)