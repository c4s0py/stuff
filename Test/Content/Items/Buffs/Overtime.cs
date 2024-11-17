using System.Security;
using System.Security.Cryptography.X509Certificates;
using Mono.CompilerServices.SymbolWriter;
using Terraria;
using Terraria.Localization;
using Terraria.ModLoader;
using Test.Content.Items.Weapons;


namespace Test.Content.Items.Buffs
{
    public class Overtime:ModBuff
    
    {
        public override void Update(Player player, ref int buffIndex)
        {
            player.GetDamage<MeleeDamageClass>() += 0.15f;
            player.GetCritChance<MeleeDamageClass>() += 15f;
        }
    }


}