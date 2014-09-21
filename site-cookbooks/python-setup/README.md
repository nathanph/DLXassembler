python-setup Cookbook
=====================
This cookbook sets up python virtual environments.

Requirements
------------
#### packages
- `python` - python-setup needs python to setup virtual environments.

Usage
-----
#### python-setup::default
Just include `python-setup` in your node's `run_list`:

```json
{
  "name":"my_node",
  "run_list": [
    "recipe[python-setup]"
  ]
}
```

Contributing
------------
TODO: (optional) If this is a public cookbook, detail the process for contributing. If this is a private cookbook, remove this section.

e.g.
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------
Authors: TODO: List authors
