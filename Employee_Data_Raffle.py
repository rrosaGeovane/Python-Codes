import os
import random

ROOT_FOLDER = 'Employee_Data'
OUTPUT_FILE = 'all_employees.txt'


def collect_names():
    all_names = []

    for i in range(1, 41):
        folder_name = f'sector{i}'
        folder_path = os.path.join(ROOT_FOLDER, folder_name)
        register_file = os.path.join(folder_path, 'registrations.txt')

        try:
            with open(register_file, 'r', encoding='utf-8') as f:
                names = [line.strip() for line in f if line.strip()]
                all_names.extend(names)
                print(f'✅ {len(names)} names read from {folder_name}')
        except FileNotFoundError:
            print(f'⚠️ File not found in {folder_name}')
        except Exception as e:
            print(f'❌ Error in {folder_name}: {str(e)}')

    return all_names


def save_names(names):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(names))
    print(f'\n📁 All names were saved in "{OUTPUT_FILE}"')


def draw_winner(names):
    if not names:
        print('No names found for the draw!')
        return None

    winner = random.choice(names)
    print('\n🎉🎊 DRAW COMPLETED 🎊🎉')
    print(f'CONGRATULATIONS TO THE WINNER: {winner}')
    return winner


if __name__ == '__main__':
    print('Starting process...\n')
    employee_names = collect_names()

    if employee_names:
        save_names(employee_names)
        draw_winner(employee_names)
    else:
        print('No employee names were found!')
