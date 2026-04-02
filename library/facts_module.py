#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import platform
import os

def main():
    module = AnsibleModule(argument_spec={})

    facts = {
        'hostname': platform.node(),
        'system': platform.system(),
        'release': platform.release(),
        'python_version': platform.python_version(),
        'user': os.getenv("USER")
    }

    module.exit_json(
        changed=False,
        ansible_facts={
            'custom_facts': facts
        }
    )

if __name__ == '__main__':
    main()
