import random

class ProjectGenerator:
    def __init__(self):
        self.FieldKeywords = {
            "web": ["Scalable", "Responsive", "Framework", "API", "Cloud", "Database", "Frontend", "Backend", "Microservices", "UserInterface"],
            "ai": ["MachineLearning", "NeuralNetwork", "Model", "Data", "Algorithm", "DeepLearning", "Prediction", "Training", "NaturalLanguageProcessing", "Chatbot"],
            "data": ["Visualization", "Processing", "Analytics", "Dataset", "BigData", "MachineLearning", "Database", "Scraping", "API", "Report"],
            "game": ["Multiplayer", "VR", "AR", "Engine", "Graphics", "Physics", "Simulation", "AI", "Character", "LevelDesign"],
            "mobile": ["Android", "iOS", "App", "GPS", "Bluetooth", "Payment", "Notification", "UserExperience", "Camera", "Location"],
            "automation": ["Script", "Scheduler", "Task", "Cron", "Monitor", "API", "Cloud", "Automation", "Database", "Integration"],
            "malware": ["Trojan", "Ransomware", "Keylogger", "Exploit", "Spyware", "Rootkit", "Phishing", "Backdoor", "Virus", "Botnet"],
            "networking": ["Firewall", "PacketSniffer", "VPN", "Protocol", "Security", "Router", "Switch", "Proxy", "Packet", "OSIModel"],
            "security": ["Encryption", "PenetrationTesting", "ThreatDetection", "Vulnerability", "Firewall", "MalwareAnalysis", "IncidentResponse", "PhishingTest", "DDoS", "XSS"],
            "cloud": ["AWS", "Azure", "Docker", "Kubernetes", "Container", "CI/CD", "Infrastructure", "Serverless", "DevOps", "CloudSecurity"],
            "blockchain": ["SmartContracts", "Cryptocurrency", "Decentralized", "NFT", "Wallet", "Ledger", "BlockchainProtocol", "Consensus", "Token", "Mining"]
        }

        self.FieldProjects = {
            "web": {
                "beginner": ["PersonalPortfolio", "Blog"],
                "moderate": ["API", "EcommerceSite"],
                "hard": ["WebApplication"],
                "advanced": ["FullStackApp", "PWA"],
                "expert": ["ScalableWebSystem", "RealTimeWebApp"]
            },
            "ai": {
                "beginner": ["AIChatbot", "ImageRecognitionModel"],
                "moderate": ["RecommendationSystem", "PredictiveAnalyticsTool"],
                "hard": ["MachineLearningModel"],
                "advanced": ["DeepLearningModel", "AIOptimisationTool"],
                "expert": ["AutonomousSystem", "AIResearchPaper"]
            },
            "data": {
                "beginner": ["DataVisualizationTool", "BasicDataAnalysisScript"],
                "moderate": ["DataScrapingScript", "SentimentAnalysisTool"],
                "hard": ["BigDataAnalysis", "DataProcessingPipeline"],
                "advanced": ["DataMiningTool", "DataWarehouseSystem"],
                "expert": ["AIDataIntegration", "RealTimeDataProcessingSystem"]
            },
            "game": {
                "beginner": ["2DGame", "TextBasedGame"],
                "moderate": ["3DGame", "AugmentedRealityGame"],
                "hard": ["VirtualRealityGame", "GameAI"],
                "advanced": ["GameEnginePlugin", "MultiplayerGame"],
                "expert": ["GameEngine", "MMORPG"]
            },
            "mobile": {
                "beginner": ["MobileApp", "SimpleMobileGame"],
                "moderate": ["FitnessTrackerApp", "ToDoApp"],
                "hard": ["MobileGame", "LocationBasedServiceApp"],
                "advanced": ["MobilePaymentSystem", "AugmentedRealityApp"],
                "expert": ["MobileCloudApp", "MobileHealthApp"]
            },
            "automation": {
                "beginner": ["AutomationScript", "SimpleTaskScheduler"],
                "moderate": ["SystemMonitoringTool", "FileOrganizer"],
                "hard": ["WebScrapingAutomation", "AdvancedTaskScheduler"],
                "advanced": ["AIAutomationTool", "CloudAutomationScript"],
                "expert": ["EnterpriseAutomationSystem", "RoboticProcessAutomation"]
            },
            "malware": {
                "beginner": ["MalwareAnalysisTool", "Keylogger"],
                "moderate": ["RansomwareSimulation", "PhishingAttackTool"],
                "hard": ["Rootkit", "BotnetSimulation"],
                "advanced": ["ExploitFramework", "AdvancedMalwareAnalysis"],
                "expert": ["MalwareReverseEngineering", "ZeroDayExploit"]
            },
            "networking": {
                "beginner": ["PacketSniffer", "SimpleFirewall"],
                "moderate": ["VPNSetup", "PacketAnalyzer"],
                "hard": ["RoutingProtocolSimulator", "NetworkIntrusionDetection"],
                "advanced": ["SDN", "AdvancedSecurityProtocol"],
                "expert": ["NetworkForensics", "AdvancedPacketCrafting"]
            },
            "security": {
                "beginner": ["EncryptionTool", "PenetrationTestingScript"],
                "moderate": ["PhishingDetectionTool", "MalwareScanner"],
                "hard": ["SecurityAudit", "ExploitDetection"],
                "advanced": ["IncidentResponsePlan", "DDoSProtectionTool"],
                "expert": ["AdvancedCryptography", "SecurityAutomation"]
            },
            "cloud": {
                "beginner": ["BasicCloudApp", "CloudStorageScript"],
                "moderate": ["AWSInstanceSetup", "ServerlessApp"],
                "hard": ["CI/CDPipeline", "DockerContainerApp"],
                "advanced": ["CloudSecuritySystem", "KubernetesCluster"],
                "expert": ["MultiCloudArchitecture", "CloudNativeApp"]
            },
            "blockchain": {
                "beginner": ["SmartContract", "BasicCryptocurrencyWallet"],
                "moderate": ["NFTMarketplace", "BlockchainExplorer"],
                "hard": ["DecentralizedExchange", "BlockchainOracle"],
                "advanced": ["PrivateBlockchain", "Layer2Solution"],
                "expert": ["BlockchainProtocolDevelopment", "CryptoMiningPool"]
            }
        }

    def GetRelatedWord(self, field):
        field = field.lower()
        return random.choice(self.FieldKeywords.get(field, ["Example"]))

    def GenerateProjectIdea(self, field, level):
        field = field.lower()
        level = level.lower()

        word1 = self.GetRelatedWord(field)
        word2 = self.GetRelatedWord(field)

        projects = self.FieldProjects.get(field, {}).get(level, self.FieldProjects.get(field, {}).get("beginner", []))
        project_type = random.choice(projects) if projects else "BasicProject"

        return f"Build a {project_type} for {word1} and {word2}"

class EntryPoint:
    def Main(self):
        print("Enter a field/topic (e.g., Web, AI, Data, Game, Mobile, Automation, Malware, Networking, Security, Cloud, Blockchain):")
        field = input().strip()

        print("Enter a difficulty level (Beginner, Moderate, Hard, Advanced, Expert):")
        level = input().strip()

        generator = ProjectGenerator()
        project_idea = generator.GenerateProjectIdea(field, level)
        print(f"Random Project Idea: {project_idea}")

    def Run(self):
        self.Main()

if __name__ == "__main__":
    entry_point = EntryPoint()
    entry_point.Run()
