# VoxelPluginBot — Suggested Support Replies

28 additional quick replies for VoxelCore, VoxelFurniture, Geyser, and general support. Your four existing replies are **not included**.

Review and edit these messages as needed before importing. Each reply has a **command**, **embed title**, **embed description**, and **embed colour**.

---

## `!!support core`

**Title:** VoxelCore | Support  
**Embed colour:** `#28B8CF`

Need help with **VoxelCore**? Please create a thread in the VoxelCore support channel and tell us what you're trying to do.

Include your **Minecraft version**, **server software**, the **exact VoxelCore JAR filename**, and any relevant logs or configuration snippets.

📖 Documentation: https://github.com/VoxelHorizons/VoxelCore/wiki
🐛 Bug reports: https://github.com/VoxelHorizons/VoxelCore/issues

---

## `!!install`

**Title:** Voxel Horizons | Installation  
**Embed colour:** `#28B8CF`

**VoxelCore** is the base plugin. **VoxelFurniture** requires VoxelCore to be installed first.

Download the **correct VoxelCore JAR for your Minecraft version**, place it in `plugins/`, and start the server. For furniture, add the universal VoxelFurniture JAR too.

📖 Core guide: https://github.com/VoxelHorizons/VoxelCore/wiki/Installation
🪑 Furniture guide: https://github.com/VoxelHorizons/VoxelFurniture/wiki/Installation

---

## `!!install core`

**Title:** VoxelCore | Installation  
**Embed colour:** `#28B8CF`

Download **one** version-specific VoxelCore JAR from the official release and put it in your server's `plugins/` folder. Start the server, then follow the installation guide to configure content and build your packs.

Do **not** install several VoxelCore server JARs together.

📦 https://github.com/VoxelHorizons/VoxelCore/releases/tag/v1.0.0
📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Installation

---

## `!!install furniture`

**Title:** VoxelFurniture | Installation  
**Embed colour:** `#28B8CF`

VoxelFurniture requires **VoxelCore v1.0.0**. Install the matching VoxelCore server JAR and `VoxelFurniture-1.0.0-mc1.12-26.3.jar` in `plugins/`, then restart the server.

Create furniture definitions through the VoxelCore content system and build the required resource pack.

📦 https://github.com/VoxelHorizons/VoxelFurniture/releases/tag/v1.0.0
📖 https://github.com/VoxelHorizons/VoxelFurniture/wiki/Installation

---

## `!!downloads`

**Title:** Voxel Horizons | Official Downloads  
**Embed colour:** `#28B8CF`

Please download the plugins from their **official release pages**.

📦 **VoxelCore:** https://github.com/VoxelHorizons/VoxelCore/releases
🪑 **VoxelFurniture:** https://github.com/VoxelHorizons/VoxelFurniture/releases

VoxelCore has separate JARs for Minecraft version families; Furniture uses one universal JAR. Avoid unofficial mirrors, reuploads or modified distributions.

---

## `!!compatibility`

**Title:** Voxel Horizons | Compatibility  
**Embed colour:** `#28B8CF`

VoxelCore provides **version-specific builds** and VoxelFurniture provides a universal JAR for supported server versions. Choose the correct Core build for your server.

Support across a version family does **not** mean every intermediate release was individually tested. **Folia is not supported.** Bedrock rendering may differ from Java.

📖 Core matrix: https://github.com/VoxelHorizons/VoxelCore/wiki/Compatibility
🪑 Furniture matrix: https://github.com/VoxelHorizons/VoxelFurniture/wiki/Compatibility

---

## `!!dependencies`

**Title:** Voxel Horizons | Dependencies  
**Embed colour:** `#28B8CF`

**VoxelCore** is the required foundation for **VoxelFurniture**. Install a compatible version of Core before installing Furniture.

**Geyser** is optional and needed only for Bedrock integration. Some integrations, such as WorldGuard, Lands and PlaceholderAPI, are also optional where supported.

If a plugin will not load, share your startup log and the exact names of the installed JAR files.

---

## `!!logs`

**Title:** Support | Server Logs  
**Embed colour:** `#28B8CF`

Please upload your server's **`logs/latest.log`** to https://mclo.gs and share the link in your support thread.

Try to reproduce the issue first, then upload a **fresh log covering the error**. Include the time it happened and what you did just beforehand.

**Remove passwords, tokens and other sensitive information** before posting anything publicly.

---

## `!!startup`

**Title:** Support | Plugin Startup Failure  
**Embed colour:** `#28B8CF`

If VoxelCore or VoxelFurniture fails to start, please share:

• Minecraft version and server software (including build)
• Exact Core/Furniture JAR filenames
• Complete startup error from `logs/latest.log` (https://mclo.gs)
• Whether this is a fresh install or an update

Check the compatibility guide and confirm **VoxelCore loads before Furniture**.

---

## `!!bedrock`

**Title:** VoxelCore | Bedrock Support  
**Embed colour:** `#28B8CF`

Bedrock support uses **Geyser** alongside VoxelCore's Bedrock pack generation and supported item/block mappings. The separate Geyser extension adds supported **entity projection** features.

Java and Bedrock may render or behave differently; full parity is **not guaranteed**.

Please include your Geyser version, VoxelCore JAR, and screenshots from **both editions** when reporting a difference.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Bedrock-and-Geyser

---

## `!!geyser`

**Title:** VoxelCore | Geyser Integration  
**Embed colour:** `#28B8CF`

Using Geyser for Bedrock players? Follow the VoxelCore **Bedrock and Geyser** guide to generate supported Bedrock assets and configure Geyser content mappings.

The Geyser extension is **optional** for additional supported entity projections; it is not another server plugin.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Bedrock-and-Geyser

---

## `!!geyser extension`

**Title:** VoxelCore | Geyser Extension  
**Embed colour:** `#28B8CF`

The **VoxelCore Geyser extension** is a **separate optional JAR** for supported entity projections on Bedrock.

Download it from the VoxelCore release, place it in your Geyser **`extensions/`** directory, and restart Geyser. Do **not** put it in Bukkit/Paper's `plugins/` folder.

📦 https://github.com/VoxelHorizons/VoxelCore/releases/tag/v1.0.0
📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Bedrock-and-Geyser

---

## `!!pack`

**Title:** VoxelCore | Resource Pack Issues  
**Embed colour:** `#28B8CF`

If custom textures, fonts or models are missing, confirm that the **correct resource pack** was successfully built and delivered to the client.

Please share the pack build/validation output, your Minecraft version, the affected content ID and a screenshot of the result. Try reconnecting after updating the pack.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Resource-Packs

---

## `!!pack bedrock`

**Title:** VoxelCore | Bedrock Pack Issues  
**Embed colour:** `#28B8CF`

If content works on **Java** but not **Bedrock**, confirm that the Bedrock pack was built, Geyser is using the intended mappings, and the client downloaded the updated pack.

Please share **Java and Bedrock screenshots**, VoxelCore/Geyser versions, pack build logs and the affected item/block/model ID.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Bedrock-and-Geyser

---

## `!!blocks`

**Title:** VoxelCore | Custom Block Problems  
**Embed colour:** `#28B8CF`

Having trouble with custom blocks? Please share the **block's namespaced ID**, its YAML definition, Minecraft version and screenshots of what is happening.

Tell us whether the issue affects **placement**, **textures**, **drops** or **Bedrock display**. Include any pack build warnings or console errors.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Custom-Blocks

---

## `!!models`

**Title:** VoxelCore | Custom Model Problems  
**Embed colour:** `#28B8CF`

If a custom model is missing, invisible or positioned incorrectly, please share the **content ID**, model definition, Minecraft version and a screenshot.

If this is a Java/Bedrock difference, include a screenshot from **each edition** plus your pack build output.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Custom-Items
📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Resource-Packs

---

## `!!ui`

**Title:** VoxelCore | UI, Fonts & Glyphs  
**Embed colour:** `#28B8CF`

For missing glyphs, incorrect menu backgrounds, tooltips or font alignment, please share a screenshot, the relevant configuration, Minecraft/client edition and your resource-pack build output.

If the problem is Bedrock-only, include an equivalent **Java screenshot** for comparison.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/UI-Fonts-and-Glyphs

---

## `!!furniture`

**Title:** VoxelFurniture | Troubleshooting  
**Embed colour:** `#28B8CF`

Please describe which furniture definition is affected and what action fails: **placing, interacting, seating, storing items or rendering**.

Share the furniture ID/YAML, Minecraft version, Core and Furniture versions, and any console errors. Include Java/Bedrock screenshots if the issue is edition-specific.

📖 https://github.com/VoxelHorizons/VoxelFurniture/wiki/Troubleshooting

---

## `!!furniture storage`

**Title:** VoxelFurniture | Storage Issues  
**Embed colour:** `#28B8CF`

For broken furniture storage, please tell us whether the inventory **does not open**, **loses items**, **shows the wrong UI** or **fails after a restart**.

Include the furniture ID, storage configuration, both plugin versions and any server errors. Avoid testing with irreplaceable items.

📖 https://github.com/VoxelHorizons/VoxelFurniture/wiki/Storage-and-Animations

---

## `!!furniture animation`

**Title:** VoxelFurniture | Animation Issues  
**Embed colour:** `#28B8CF`

For animations or model-state problems, please share the furniture definition, the state transition you're expecting and what actually happens. A short video or before/after screenshots help a lot.

Mention whether the problem occurs on **Java, Bedrock or both**.

📖 https://github.com/VoxelHorizons/VoxelFurniture/wiki/Storage-and-Animations

---

## `!!furniture protection`

**Title:** VoxelFurniture | Protection Issues  
**Embed colour:** `#28B8CF`

If furniture placement, breaking or interaction behaves incorrectly in protected regions, tell us which protection plugin you're using (**WorldGuard, Lands or neither**), the relevant region rules and what you expected.

Include your Minecraft version, Core/Furniture versions and whether the player has administrator privileges.

📖 https://github.com/VoxelHorizons/VoxelFurniture/wiki/Protection

---

## `!!permissions`

**Title:** Voxel Horizons | Permissions  
**Embed colour:** `#28B8CF`

If a command or interaction says **no permission**, check your permissions plugin and the relevant permission nodes. VoxelFurniture's basic place, break, sit and inventory permissions are enabled by default; administrative actions are restricted.

Share the **exact command/action**, permission error and affected player's role.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Commands-and-Administration

---

## `!!update`

**Title:** Voxel Horizons | Updating Plugins  
**Embed colour:** `#28B8CF`

Before updating, **back up** your plugin data, content definitions, generated packs and persistent world data.

Download the new official release and confirm the VoxelCore build matches your Minecraft version. Check compatibility with your Furniture build before replacing JARs.

📖 https://github.com/VoxelHorizons/VoxelCore/wiki/Upgrading-and-Backups
📦 https://github.com/VoxelHorizons/VoxelCore/releases

---

## `!!bug`

**Title:** Voxel Horizons | Reporting a Bug  
**Embed colour:** `#28B8CF`

Found a reproducible bug? Please include:

• Plugin and Minecraft/server versions
• Exact steps to reproduce
• Expected result vs actual result
• `latest.log` link from https://mclo.gs
• Screenshots/video or minimal configuration if relevant

🐛 **VoxelCore:** https://github.com/VoxelHorizons/VoxelCore/issues
🪑 **VoxelFurniture:** https://github.com/VoxelHorizons/VoxelFurniture/issues

Please report security vulnerabilities **privately**, not in public issues.

---

## `!!feature`

**Title:** Voxel Horizons | Feature Requests  
**Embed colour:** `#28B8CF`

Have an idea for VoxelCore or VoxelFurniture? We'd love to hear it!

Please explain the **use case**, how you expect it to work and why it would help server owners. Screenshots, mockups and examples are welcome.

Check existing issues first so we can keep related suggestions together.

📦 https://github.com/VoxelHorizons/VoxelCore/issues
🪑 https://github.com/VoxelHorizons/VoxelFurniture/issues

---

## `!!security`

**Title:** Voxel Horizons | Security Reports  
**Embed colour:** `#E67E22`

Please **do not post exploits, credentials, private server data or vulnerability reproduction steps in public Discord threads**.

Use the relevant repository's security policy for the proper private disclosure route:

📦 https://github.com/VoxelHorizons/VoxelCore/blob/main/SECURITY.md
🪑 https://github.com/VoxelHorizons/VoxelFurniture/blob/main/SECURITY.md

This helps us investigate without exposing other servers to risk.

---

## `!!license`

**Title:** Voxel Horizons | Usage & Licensing  
**Embed colour:** `#28B8CF`

VoxelCore and VoxelFurniture are **free to use and source-available**. You may run them on your server, including monetised servers, and privately customise them within their licence terms.

Unauthorised rehosting, redistribution, repackaging and resale are not permitted, subject to applicable authorised-platform rights. They are **not OSI-approved open-source**.

📄 https://github.com/VoxelHorizons/VoxelCore/blob/main/LICENSE.md
🪑 https://github.com/VoxelHorizons/VoxelFurniture/blob/main/LICENSE.md

---

## `!!vehicles`

**Title:** VoxelVehicles | Availability  
**Embed colour:** `#28B8CF`

**VoxelVehicles** is currently a **private/commercial Voxel Horizons plugin** and is not available for public purchase or download yet.

We'll announce an official sales channel when it's ready. Please don't download or share unofficial copies.

For questions about existing authorised installations, use the **VoxelVehicles support channel**.

---
