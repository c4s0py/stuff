using Terraria.ID;
using Terraria.ModLoader;
using Terraria.Localization;
using Terraria.GameContent.Creative;

namespace Test.Content.Items.Materials
{
    public class DullBlade : ModItem
    {
        public override void SetDefaults()
        {
            Item.width = 24;
            Item.height = 24;
            Item.maxStack = 1;
            Item.value = 10000;
            Item.rare = ItemRarityID.Lime;
        }
    }

}