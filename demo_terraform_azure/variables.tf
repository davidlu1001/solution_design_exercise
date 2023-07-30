variable "resource_group_name" {
  type        = string
  description = "Name of the resource group."
  validation {
    condition     = length(var.resource_group_name) <= 10
    error_message = "Resource group name must be 10 characters or less."
  }
  default = "example-resource-group"
}

variable "location" {
  type        = string
  description = "Azure region where the resources will be deployed."
  default     = "East US"
}

variable "virtual_network_name" {
  type        = string
  description = "Name of the virtual network."
  default     = "virtnetname"
}

variable "virtual_network_address_space" {
  type        = list(string)
  description = "Address space for the virtual network."
  default     = ["10.0.0.0/16"]
}

variable "subnet_name" {
  type        = string
  description = "Name of the subnet."
  default     = "subnetname"
}

variable "subnet_address_prefixes" {
  type        = list(string)
  description = "Address prefixes for the subnet."
  default     = ["10.0.2.0/24"]
}

variable "storage_account_name" {
  type        = string
  description = "Name of the storage account."
  validation {
    condition     = can(regex("^[a-z0-9]{3,24}$"), var.storage_account_name)
    error_message = "Storage account name must be 3 to 24 characters long, lowercase alphanumeric only."
  }
  default = "storageaccountname"
}

variable "storage_account_tier" {
  type        = string
  description = "Storage account tier."
  default     = "Standard"
}

variable "storage_account_replication_type" {
  type        = string
  description = "Storage account replication type."
  default     = "LRS"
}

variable "tags" {
  type        = map(string)
  description = "Tags to be assigned to the resources."
  default = {
    environment = "demo"
  }
}
