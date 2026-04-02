#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=False, default='student')
        )
    )

    name = module.params['name']

    result = {
        'changed': False,
        'message': f'Hello, {name}! This is custom info module.'
    }

    module.exit_json(**result)

if __name__ == '__main__':
    main()
