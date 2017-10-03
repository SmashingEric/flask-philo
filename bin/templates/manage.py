import os
import sys
import argparse


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, '../'))


def main():
    from flaskutils import init_app, execute_command
    description = 'Manage flask application'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('command', help='command to execute')

    # isolate test and development database configurations
    if parser.parse_known_args()[0].command == "test":
        parser.add_argument(
            '--settings',
            help='config file path',
            default='config.test')
    else:
        parser.add_argument(
            '--settings',
            help='config file path',
            default='config.development')

    args, extra_params = parser.parse_known_args()
    os.environ.setdefault('FLASKUTILS_SETTINGS_MODULE', args.settings)

    init_app(__name__, BASE_DIR)
    print("execute_command : ", args.command)
    execute_command(args.command)


if __name__ == '__main__':
    main()
