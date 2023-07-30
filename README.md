# Diagram - Azure Architecture Design

This diagram showcases the high-level architecture design for the Flight Information System based on Azure services.

![Azure Architecture Design](https://github.com/davidlu1001/solution_design_exercise/blob/55fc460f7aa427ab85dd1ee0a03ea9e126f55a0f/arch_diagram/arch_diagram.png?raw=true)

P.S.

The architecture diagram is generated using the open-source tool called "diagrams" available on GitHub. For more information about the "diagrams" tool and its features, please visit the GitHub repository at: https://github.com/mingrammer/diagrams.

## Components and Services

- **On-prem Network:** Represents the on-premises private network where virtual machines (VMs) reside.
- **Users:** Represents the end-users accessing the system.
- **Azure Active Directory (AAD):** Manages user authentication and access control.
- **Internet:** Represents the public internet.
- **Azure DNS:** Provides domain name resolution for the system.
- **Azure Front Door (WAF / CDN):** Acts as a Web Application Firewall (WAF) and Content Delivery Network (CDN) to optimize global web app performance and secure against web-based attacks.
- **Azure DDoS Protection Plan**: Provides dedicated network-layer DDoS protection.
- **VPN Gateway:** Connects the on-premises network to the Azure virtual network securely.
- **Azure Firewall:** Provides network security and filtering capabilities for the virtual network.
- **App Services:** Hosts the web app and API services in Azure.
- **Service Bus:** Facilitates messaging and communication between web apps and API services.
- **Blob Storage:** Stores unstructured data like media files.
- **Virtual Network:** Provides isolation and security for the web app, API, and other resources.
- **SQL Databases:** Hosts the primary and secondary databases for data storage.
- **Redis Cache:** Caches frequently accessed data to improve performance.
- **Key Vaults:** Securely manages keys, secrets, and certificates used in the system.
- **Monitoring / Logging:** Includes Azure Monitor, Application Insights, and Log Analytics for monitoring and logging capabilities.

## Connections

- Users connect to the system through the Internet and Azure Front Door.
- On-premises network connects to Azure through VPN Gateway.
- Azure Front Door connects to the Virtual Network to route traffic to the Web App and API Service.
- App Services interact with Redis Cache, Service Bus, and Blob Storage for data operations.
- Primary and Secondary Databases communicate with the web apps for data storage.
- Monitoring and Logging services collect data from different components for observability.

## Note

- Geo-Replication for the databases is not shown for better layout.

## How to Install Diagrams

You can install `diagrams` using `pip` or `pdm`.

### Using pip

To install `diagrams` using `pip`, open a terminal or command prompt and run the following command:

```bash
pip install diagrams
```

## How to Generate the Architecture Diagram
Once you have diagrams installed, you can generate the architecture diagram by running the diagram.py script:

```bash
python diagram.py
```

The script will create a PNG image named `arch_diagram.png` that represents the architecture design.
