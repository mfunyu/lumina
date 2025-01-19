[README](README.md) • [Concept & Design (en)](CONCEPT.md)

[![wakatime](https://wakatime.com/badge/user/08071e9d-f227-4ac4-acb0-e78a5829cf60/project/0628c6fd-9ef4-4bec-b62d-ead7a5acae4c.svg)](https://wakatime.com/badge/user/08071e9d-f227-4ac4-acb0-e78a5829cf60/project/0628c6fd-9ef4-4bec-b62d-ead7a5acae4c)

# 🏘️💡Lumina

Lumina is an advanced system **designed to connect homes worldwide**, making them **autonomous and highly efficient**. It enhances convenience by automating tasks, controlling home environments remotely, and providing custom routines for users.

Lumina optimizes energy usage, promotes the use of renewable energy, and encourages environmental responsibility. It also focuses on safety and accessibility, offering assistance to individuals with disabilities or the elderly and monitoring the health and safety of all residents.

This innovative solution aims to transform how we interact with and manage our homes, creating a smarter, greener, and more inclusive living environment.

## Usage

| Dashboard | Config | About |
| :--: | :--: | :--: |
| <img width="479" alt="Capture d’écran 2024-07-01 à 11 33 26" src="https://github.com/mfunyu/lumina/assets/60470877/699f2b77-8fa5-40de-82d3-eead215b7953"> | <img width="476" alt="Capture d’écran 2024-07-01 à 11 30 35" src="https://github.com/mfunyu/lumina/assets/60470877/73acb0c5-2626-4375-bed0-559875ef94d1"> | <img width="475" alt="Capture d’écran 2024-07-01 à 11 28 53" src="https://github.com/mfunyu/lumina/assets/60470877/72d7fe8d-a377-489e-adc6-71ebdee9ad9e"> |
| <img width="479" alt="Capture d’écran 2024-07-01 à 11 28 34" src="https://github.com/mfunyu/lumina/assets/60470877/d651efdb-f784-43b8-9a62-2b2aa93c788e"> | <img width="477" alt="Capture d’écran 2024-07-01 à 11 34 10" src="https://github.com/mfunyu/lumina/assets/60470877/a22c2a35-3e1a-41b1-936f-61739b9c3165"> | <img width="477" alt="Capture d’écran 2024-07-01 à 11 34 28" src="https://github.com/mfunyu/lumina/assets/60470877/615f50a4-2256-4e6b-a206-45653cfd4004">

## ⚙️Installation

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mfunyu/lumina.git
   ```

2. Set environment variables
   ```
   make setup
   ```

3. Start the docker containers:
   ```
   make
   ```

4. Access from a browser: https://localhost:8080



## Development Planning

| Étape                         | Description                                    | Jour       | Estimated Time       |
|-------------------------------|------------------------------------------------|------------|----------------------|
| **Étape 1 : Setup**         |                                                |            |                      |
| ✅ 1.1 Développement du idée     | Écrire des tests pour les fonctionnalités      | Jour 1     | 3 hours              |
| **Étape 2 : Backend**         |                                                |            |                      |
| ✅ 2.1 Développement du test     | Écrire des tests pour les fonctionnalités      | Jour 2     | 1 hours              |
| ✅ 2.2 Développement du backend  | Implémentation du backend pour passer les tests| Jour 2     | 1 hours              |
| **Étape 3 : Frontend**        |                                                |            |                      |
| ✅ 3.1 Design                    | Conception et stylisation du frontend          | Jour 3     | 4 hours              |
| ✅ 3.2 Développement basic       | Développement de la structure de base du frontend | Jour 4 | 4 hours              |
| ✅ 3.3 Finalisation              | Finalisation des fonctionnalités du frontend   | Jour 5     | 2 hours              |
| **Étape 4 : Connexion Full-Stack** |                                            |            |                      |
| ✅ 4.1 Intégration du backend    | Connecter le backend au frontend               | Jour 6     | 8 hours              |
| ✅ 4.2 Intégration du frontend   | S'assurer que le frontend fonctionne avec le backend | Jour 7 | 8 hours              |
| **Étape 5 : Text-to-Speech**  |                                                |            |                      |
| ✅ 5.1 Développement             | Implémentation de la fonctionnalité Text-to-Speech | Jour 8 | 8 hours              |
| **Étap 6 : Bonus**                     | Temps supplémentaire en cas de retard ou ajustements | Jour 9-10 | 16 hours total |
