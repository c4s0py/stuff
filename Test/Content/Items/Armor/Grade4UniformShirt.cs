using Terraria;
using Terraria.GameContent.RGB;
using Terraria.ID;
using Terraria.Localization;
using Terraria.ModLoader;
using Test.Content.Items.Buffs;


namespace Test.Content.Items.Armor
{

    [AutoloadEquip(EquipType.Body)]
    public class Grade4UniformShirt:ModItem
    {
        public static readonly int MaxManaIncrease = 20;

        public override LocalizedText Tooltip => base.Tooltip.WithFormatArgs(MaxManaIncrease);
        public override void SetDefaults()
        {
            Item.width = 18;
            Item.height = 18;
            Item.value = Item.sellPrice(gold:1);
            Item.rare = ItemRarityID.Green;
            Item.defense = 8;
        }



        public override void UpdateEquip(Player player)
        {
            player.statManaMax2 += MaxManaIncrease;
        }

    }









    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    }