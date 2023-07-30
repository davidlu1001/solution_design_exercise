from diagrams import Cluster, Diagram, Edge
from diagrams.azure.compute import AppServices
from diagrams.onprem.network import Internet
from diagrams.aws.management import SystemsManagerDocuments
from diagrams.aws.media import MediaServices
from diagrams.azure.database import BlobStorage, CacheForRedis, SQLDatabases, CosmosDb
from diagrams.azure.storage import BlobStorage
from diagrams.azure.identity import ActiveDirectory, Users
from diagrams.azure.network import DDOSProtectionPlans, DNSPrivateZones, DNSZones, Firewall, FrontDoors, LocalNetworkGateways, Subnets, VirtualNetworkGateways
from diagrams.azure.security import KeyVaults
from diagrams.azure.integration import ServiceBus
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.general import Servicehealth
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.compute import VM

with Diagram(show=False, direction="TB"):
    users = Users("Users")
    aad = ActiveDirectory("Azure Active Directory")
    internet = Internet("Internet")
    dns = DNSZones("Azure DNS")

    frontdoor = FrontDoors("Front Door (WAF / CDN)")

    # On-prem
    with Cluster("On-prem Network", direction="LR"):
        vms = [VM("Virtual Machine")]
        local_gw = LocalNetworkGateways("Local Gateway")

    # Primary Region
    with Cluster("Primary Region"):
        with Cluster("DDoS Protection"):
            with Cluster("Hub Virtual Network"):
                fw_1 = Firewall("Azure Firewall")
                vpn_gw_1 = VirtualNetworkGateways("VPN Gateway")

        with Cluster("App Service"):
            webapp_1 = AppServices("Web App")
        with Cluster("Service Bus"):
            servicebus_1 = ServiceBus("Service Bus")
        with Cluster("API Service"):
            apiapp_1 = AppServices("API App")
        with Cluster("Blob", direction="LR"):
            blob_1 = BlobStorage("Blob")
            media_1 = MediaServices("Media")
        with Cluster("Virtual Network"):
            webapp_subnet_1 = Subnets("Web App Subnet")
            api_subnet_1 = Subnets("API App Subnet")
            private_endpiont_subnet_1 = Subnets("Private Endpoint Subnet")
    
    db_1 = SQLDatabases("Database - Primary")

    dns_zones_1 = DNSPrivateZones("DNS Zones")
    redis_1 = CacheForRedis("Redis Cache")
    keyvault_1 = KeyVaults("Key Vault")

    # Secondary Region
    with Cluster("Secondary Region"):
        with Cluster("DDoS Protection"):
            with Cluster("Hub Virtual Network"):
                fw_2 = Firewall("Azure Firewall")
                vpn_gw_2 = VirtualNetworkGateways("VPN Gateway")
        with Cluster("App Service"):
            webapp_2 = AppServices("Web App")
        with Cluster("Service Bus"):
            servicebus_2 = ServiceBus("Service Bus")
        with Cluster("API Service"):
            apiapp_2 = AppServices("API App")
        with Cluster("Blob", direction="LR"):
            blob_2 = BlobStorage("Blob")
            media_2 = MediaServices("Media")
        with Cluster("Virtual Network"):
            webapp_subnet_2 = Subnets("Web App Subnet")
            api_subnet_2 = Subnets("API App Subnet")
            private_endpiont_subnet_2 = Subnets("Private Endpoint Subnet")
    
    db_2 = SQLDatabases("Database - Secondary")

    dns_zones_2 = DNSPrivateZones("DNS Zones")
    redis_2 = CacheForRedis("Redis Cache")
    keyvault_2 = KeyVaults("Key Vault")

    # Monitoring / Logging
    with Cluster("Monitoring / Logging", direction="TB"):
        monitor = Servicehealth("Azure Monitor")
        application_insights = ApplicationInsights("Application Insights")
        log_analytics = LogAnalyticsWorkspaces("Log Analytics")

    # Draw
    users >> internet >> frontdoor
    aad << internet >> dns

    local_gw >> vpn_gw_1
    local_gw >> vpn_gw_2

    frontdoor >> vpn_gw_1 - fw_1 - webapp_subnet_1
    webapp_1 << redis_1 << db_1
    webapp_1 >> servicebus_1 >> apiapp_1
    webapp_1 >> blob_1
    webapp_1 >> webapp_subnet_1 >> dns_zones_1
    apiapp_1 >> api_subnet_1 >> dns_zones_1
    private_endpiont_subnet_1 >> dns_zones_1
    private_endpiont_subnet_1 >> keyvault_1
    private_endpiont_subnet_1 >> redis_1
    private_endpiont_subnet_1 >> db_1

    frontdoor >> vpn_gw_2 - fw_2 - webapp_subnet_2
    webapp_2 << redis_2 << db_2
    webapp_2 >> servicebus_2 >> apiapp_2
    webapp_2 >> blob_2
    webapp_2 >> webapp_subnet_2 >> dns_zones_2
    apiapp_2 >> api_subnet_2 >> dns_zones_2
    private_endpiont_subnet_2 >> dns_zones_2
    private_endpiont_subnet_2 >> keyvault_2
    private_endpiont_subnet_2 >> redis_2
    private_endpiont_subnet_2 >> db_2

    # Comment for better layout
    #db_1 >> Edge(color="black", style="dashed", label="Geo Replication") >> db_2