using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Test.Content.Items.Materials;
using Microsoft.Xna.Framework;
using Terraria.Audio;
using Microsoft.Build.Evaluation;
using Microsoft.CodeAnalysis;
using Test.Content.Items.Buffs;
using System.Security.Cryptography.X509Certificates;
using Terraria.GameContent;



namespace Test.Content.Items.Weapons
{ 
	// This is a basic item template.
	// Please see tModLoader's ExampleMod for every other example:
	// https://github.com/tModLoader/tModLoader/tree/stable/ExampleMod
	public class AwakenedBlade : ModItem
	{
		// The Display Name and Tooltip of this item can be edited in the 'Localization/en-US_Mods.Test.hjson' file.
		public override void SetDefaults()
		{
			Item.damage = 65;
			Item.DamageType = DamageClass.Melee;
			Item.width = 40;
			Item.height = 40;
			Item.useTime = 10;
			Item.useAnimation = 20;
			Item.useStyle = ItemUseStyleID.Swing;
			Item.knockBack = 10;
			Item.value = Item.buyPrice(silver: 1);
			Item.rare = ItemRarityID.Orange;
			Item.UseSound = SoundID.Item1;
			Item.autoReuse = true;
			Item.crit = 1;
			if (Main.dayTime == false)
			{
				Item.damage = 2500;
			}
		}

		public override void AddRecipes()
		{
			Recipe recipe = CreateRecipe();
			recipe.AddIngredient<RatioBlade>(1);
			recipe.AddTile(TileID.WorkBenches);
			recipe.Register();
		}

        public override void MeleeEffects(Player player, Rectangle hitbox)
        {
			if (Main.rand.NextBool(5))
			{
				Dust.NewDust(new Vector2(hitbox.X, hitbox.Y), hitbox.Width, hitbox.Height, DustID.Electric, 0,0,125);
				Dust.NewDust(new Vector2(hitbox.X, hitbox.Y), hitbox.Width, hitbox.Height, DustID.LifeDrain, 0,0,125);
			}
        }
        public override bool AltFunctionUse(Player player)
        {
            return true;
        }

        public override bool CanUseItem(Player player){
            if (player.altFunctionUse ==2){
				Item.useStyle = ItemUseStyleID.Swing;
				Item.useTime = 50;
				Item.useAnimation = 50;
				Item.damage = 130;
				Item.shoot = ProjectileID.None;
			}
			else{
				Item.useStyle = ItemUseStyleID.Swing;
				Item.useTime = 10;
				Item.useAnimation = 20;
				Item.damage = 65;
				Item.shoot = ProjectileID.None;
			}
			return base.CanUseItem(player);
        }




    }
}
