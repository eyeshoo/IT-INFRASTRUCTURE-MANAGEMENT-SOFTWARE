import pandas as pd

# Create a DataFrame with the provided data
data = {
    'Requirement ID': ['REQ-001', 'REQ-002', 'REQ-003', 'REQ-004', 'REQ-005', 'REQ-006', 'REQ-007', 'REQ-008', 'REQ-009', 'REQ-010', 'REQ-011', 'REQ-012', 'REQ-013', 'REQ-014', 'REQ-015'],
    'Requirement Description': ['Display Admin Dashboard', 'Resource Allocation in Admin', 'Task Overview in Admin', 'Approve Request in Admin', 'Detailed Financials in Admin', 'Expenditure Overview in CEO', 'Team Resource Allocation in Manager', 'Project Progress in Manager', 'Project Expenditure in Manager', 'Tasks Timeline in Manager', 'Employee Dashboard in User', 'Resource Request in User', 'Task Overview in User', 'Request Approval in User', 'Detailed Financials in User'],
    'Source': ['Customer Request', 'Product Specification', 'Internal Stakeholder Request', 'Customer Request', 'Product Specification', 'Customer Request', 'Internal Stakeholder Request', 'Product Specification', 'Customer Request', 'Internal Stakeholder Request', 'Product Specification', 'Customer Request', 'Internal Stakeholder Request', 'Product Specification', 'Customer Request'],
    'Priority': ['High', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium'],
    'Status': ['In Progress', 'Open', 'Closed', 'Open', 'In Progress', 'Open', 'In Progress', 'Closed', 'In Progress', 'Open', 'In Progress', 'Open', 'Closed', 'In Progress', 'In Progress'],
    'Traceability Links': ['Code: admin.py', 'Design: admin.py, Test: admin_test.py', 'Test: admin_test.py, Code: admin.py', 'Design: admin.py, Test: admin_test.py', 'Code: admin.py, Design: admin_design.py', 'Design: ceo.py, Test: ceo_test.py', 'Code: manager.py, Design: manager_design.py', 'Test: manager_test.py, Code: manager.py', 'Design: manager_design.py, Code: manager.py', 'Test: manager_test.py, Code: manager.py', 'Design: user_design.py, Code: user.py', 'Test: user_test.py, Code: user.py', 'Code: user.py, Test: user_test.py', 'Design: user_design.py, Test: user_test.py', 'Code: user.py, Design: user_design.py']
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file_path = 'requirements_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'The Excel file has been created: {excel_file_path}')
