using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Test.Content.Items.Materials;
using Microsoft.Xna.Framework;
using Terraria.Audio;
using Terraria.GameContent;



namespace Test.Content.Items.Weapons
{ 
	// This is a basic item template.
	// Please see tModLoader's ExampleMod for every other example:
	// https://github.com/tModLoader/tModLoader/tree/stable/ExampleMod
	public class RatioBlade : ModItem
	{
		// The Display Name and Tooltip of this item can be edited in the 'Localization/en-US_Mods.Test.hjson' file.
		public override void SetDefaults()
		{
			Item.damage = 25;
			Item.DamageType = DamageClass.Melee;
			Item.width = 40;
			Item.height = 40;
			Item.useTime = 10;
			Item.useAnimation = 20;
			Item.useStyle = ItemUseStyleID.Swing;
			Item.knockBack = 5;
			Item.value = Item.buyPrice(silver: 1);
			Item.rare = ItemRarityID.Orange;
			Item.UseSound = SoundID.Item1;
			Item.autoReuse = true;
		}

		public override void AddRecipes()
		{
			Recipe recipe = CreateRecipe();
			recipe.AddIngredient<DullBlade>(1);
			recipe.AddIngredient<CursedRags>(1);
			recipe.AddTile(TileID.WorkBenches);
			recipe.Register();
		}








    }
}
