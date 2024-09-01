# Deadlock Data Repository
A data repository the game [Deadlock](https://store.steampowered.com/app/1422450/Deadlock/) by [Valve](https://www.valvesoftware.com/).


> 🚧 **Work in progress** 🚧 \
> Currently, this repository is in the early stages of development. 
> We are working on extracting data from the game files and organizing it in a structured way. 
> If you would like to contribute, please see the [Contributing](#contributing) section below.



## 📊 Data
Data is stored in the `data` directory. Each subdirectory contains data for a specific dataset.

```plaintext
data/
├── heroes/
├── items/
└── stat-icons/
```

**Legend:**
1. The `/heroes` directory contains a subdirectory for each hero. 
Each hero subdirectory contains data in JSON format for the hero as well as assets.
Assets include images of the hero (e.g. thumbnail), as wells as icons and short videos for the hero's abilities.

2. The `/items` directory contains a subdirectory for each item.
Each item subdirectory contains data in JSON format for the item as well as the item's icon.

3. The `stat-icons` directory contains icons for the hero stats. 
See [deadlocked.wiki](https://deadlocked.wiki) for more information.

## 📝 TODOs 
- [ ] Add avatar images (e.g. full model images, headshots) for all heroes (so far only thumbnail images are available)
- [ ] Add ability data for all heroes
- [ ] Add item data for all items
- [ ] Implement CLI for data extraction from the game files

## 🎨 Contributing
Contributions are welcome! \
Create a pull request with your changes and we will review it.

