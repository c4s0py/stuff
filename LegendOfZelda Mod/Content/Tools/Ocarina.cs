using Terraria;
using Terraria.Audio;
using Terraria.ID;
using Terraria.ModLoader;
using Terraria.ModLoader.Config;

namespace test.Content.Tools
{
    public class Ocarina : ModItem
    {
        int num = 0;

        SoundStyle SunsSong = new SoundStyle("test/Content/Sounds/SunsSong");
        public override void SetDefaults()
        {
            Item.width = 5;
            Item.height = 5;
            Item.maxStack = 1;
            Item.value = 100;
            Item.useStyle = ItemUseStyleID.HoldUp;
            Item.rare = ItemRarityID.Orange;
            // Set other Item.X values here
        }


        public override void UseAnimation(Player player)
        {
            num ^= 1;
            SoundEngine.PlaySound(SunsSong);
            if (num == 1){
                Main.dayTime = false;
                Main.time = 0;
            }
            if (num == 0){
                Main.dayTime = true;
                Main.time = 15000;
            }

            
        }
    }
}