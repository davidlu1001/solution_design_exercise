output "resource_group_id" {
  value       = azurerm_resource_group.example.id
  description = "The ID of the resource group."
}

output "virtual_network_id" {
  value       = azurerm_virtual_network.example.id
  description = "The ID of the virtual network."
}

output "subnet_id" {
  value       = azurerm_subnet.example.id
  description = "The ID of the subnet."
}

output "storage_account_id" {
  value       = azurerm_storage_account.example.id
  description = "The ID of the storage account."
}
