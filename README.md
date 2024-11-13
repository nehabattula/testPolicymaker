# Azure Function Integration with VS Code and Flask UI

This project demonstrates setting up and deploying an Azure Function using VS Code, integrating Azure OpenAI services, blob storage, and a Flask UI for interaction and testing.

---

## Prerequisites - VS Code Extensions (Good to Have)

- Azure Tools
- Azure App Service
- Azure Storage
- Azure Databases
- Azure Account
- Azure Resources
- Azure Functions
- Python Debugger

---

## 1. Create an Azure OpenAI Resource

### Steps:
1. Go to the [Azure Portal](https://portal.azure.com) and search for "Azure OpenAI".
2. Create a new Azure OpenAI Service:
   - Click "Create".
   - Select your Subscription and Resource Group.
   - Enter a name for the service (e.g., `OpenAIService`).
   - Choose a Region and select a Pricing Tier.
   - Click "Review + Create" and then "Create".

### Retrieve Environment Variables:
- **Azure OpenAI Key**:  
  Navigate to AzureAI Services > Azure OpenAI > Select instance `<OpenAIService>` > Resource Management > Keys and Endpoint > Select Key1 or Key2.
- **AZURE_OPENAI_ENDPOINT**:  
  Navigate to AzureAI Services > Azure OpenAI > Select instance `<OpenAIService>` > Resource Management > Keys and Endpoint > Select Endpoint.

---

## 2. Create an Azure Storage Account (For Blob Storage)

### Steps:
1. Go to the [Azure Portal](https://portal.azure.com) and search for "Storage accounts".
2. Create a new Storage Account:
   - Click "Create".
   - Select your Subscription and Resource Group.
   - Enter a Storage Account Name (e.g., `mystorageaccount`).
   - Select the Region and configure Performance/Redundancy options as needed.
   - Click "Review + Create" and then "Create".
3. Create a Container for Blob Storage:
   - Go to your storage account.
   - Click on "Containers" and create a new container (e.g., `policy-documents`).
   - Set the public access level to "Private".

### Retrieve Connection String:
- **AZURE_STORAGE_CONNECTION_STRING**:  
  Navigate to Storage Account > `<Storage Acc>` > Security + Networking > Access Keys > Connection String.

---

## 3. Create and Deploy an Azure Function

### Manual Creation (If Needed):
- Manually create `my-demo-func` in Azure if facing issues with console creation. Alternatively, you can use the Azure Function VS Code extension for deployment.

### Create a New Function App:
1. Go to the Azure Portal and click "Create".
2. Select your Subscription and Resource Group.
3. Enter a Name (e.g., `OpenAIFunctionApp`).
4. Choose "Code" as the publishing option and Python as the runtime stack.
5. Select a Region and choose the Plan Type (e.g., Consumption Plan).
6. Click "Review + Create" and then "Create".

### Local Setup (Optional but Recommended):
1. **Install Azure Functions Core Tools:**
   - Set the `func` path in the environment: `C:\Program Files\Azure Functions Core Tools`.
   - Verify installation:
     ```bash
     func --version
     ```
2. **Create a New Function Project:**
   ```bash
   mkdir <your-function-project-directory>
   cd <your-function-project-directory>
   func init --python
   func new
