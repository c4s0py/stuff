using Terraria;
using Terraria.ID;
using Terraria.Localization;
using Terraria.ModLoader;

namespace Test.Content.Items.Armor
{
    [AutoloadEquip(EquipType.Legs)]
    public  class Grade4UniformLegs : ModItem
    {
        public static readonly int ManaBonus = 10;
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
            player.statManaMax2 += ManaBonus;
        }



    }





}