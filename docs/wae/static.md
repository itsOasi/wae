# Static Folder

## Summary
The static folder holds all the project specific content, such as components, exhibits, service workers, etc.

When the engine first starts up, it finds the ```repo``` field in the ```wae_config.json``` file and  ```git clone```s the ```static``` branch into the working directory.