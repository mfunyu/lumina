[README](README.md) • [Concept & Design (en)](CONCEPT.md)

[![wakatime](https://wakatime.com/badge/user/08071e9d-f227-4ac4-acb0-e78a5829cf60/project/0628c6fd-9ef4-4bec-b62d-ead7a5acae4c.svg)](https://wakatime.com/badge/user/08071e9d-f227-4ac4-acb0-e78a5829cf60/project/0628c6fd-9ef4-4bec-b62d-ead7a5acae4c)

# 🏘️💡Lumina

## Concept Story

Lumina is an advanced system **designed to connect homes worldwide**, making them **autonomous and highly efficient**. It enhances convenience by automating tasks, controlling home environments remotely, and providing custom routines for users.

Lumina optimizes energy usage, promotes the use of renewable energy, and encourages environmental responsibility. It also focuses on safety and accessibility, offering assistance to individuals with disabilities or the elderly and monitoring the health and safety of all residents.

This innovative solution aims to transform how we interact with and manage our homes, creating a smarter, greener, and more inclusive living environment.

## This Project

This project, envisioned as an integral part of the Lumina ecosystem, is designed to function as a versatile dashboard for monitoring and controlling connected devices. With its user-friendly interface, it empowers users to register new devices, modify existing ones, and manage devices within specific rooms. Additionally, the dashboard provides advanced filtering options based on device categories and allows seamless control of device statuses, ensuring an efficient and intuitive smart home experience.

## Design - Dashboard

| Dashboard | Config | About |
| :--: | :--: | :--: |
| ![Image](https://github.com/user-attachments/assets/b01dbd7d-4470-468d-8f6f-72ca24e238e4) | ![Image](https://github.com/user-attachments/assets/05c82d78-9937-43ef-bf2f-e4c8ae967a03) | ![Image](https://github.com/user-attachments/assets/2b03e239-e37a-43d5-ad08-50d09e908f17) |
| ![Image](https://github.com/user-attachments/assets/9f85cc45-5401-46da-a0e1-cd2bdc9ddebe) | ![Image](https://github.com/user-attachments/assets/cc23f39c-c5cc-44df-be87-1e488de824e0) | ![Image](https://github.com/user-attachments/assets/b76a6ec8-7623-4a32-9106-3d1f0933ef11)


# ⚙️Installation

## Steps
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
