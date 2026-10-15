

import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as file:
        json.dump(tarefas, file, indent=4, ensure_ascii=False)


def listar_tarefas(tarefas):
    if not tarefas:
        print("\n[!] Nenhuma tarefa cadastrada.")
        return
    print("\n--- SUAS TAREFAS ---")
    for i, t in enumerate(tarefas, 1):
        status = "✔" if t["concluida"] else "❌"
        print(f"{i}. [{status}] {t['titulo']}")
    print("-------------------")


def adicionar_tarefa(tarefas):
    titulo = input("\nDigite o nome da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        salvar_tarefas(tarefas)
        print("✔ Tarefa adicionada com sucesso!")
    else:
        print("[!] O título não pode ser vazio.")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        idx = int(input("\nDigite o número da tarefa a concluir: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            salvar_tarefas(tarefas)
            print("✔ Tarefa marcada como concluída!")
        else:
            print("[!] Número inválido.")
    except ValueError:
        print("[!] Digite um número válido.")


def main():
    tarefas = carregar_tarefas()
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Concluir Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("[!] Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
