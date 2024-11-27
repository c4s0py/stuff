using System;
using System.Xml.Serialization;
using Microsoft.Build.Construction;
using Microsoft.Build.Evaluation;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Input;
using Terraria;
using Terraria.Audio;
using Terraria.Enums;
using Terraria.ID;
using Terraria.ModLoader;

namespace test.Content.Projectiles{
    public class MasterBeam:ModProjectile{
        public override void SetDefaults()
        {
            Projectile.Size = new Vector2(30);
            Projectile.friendly = true;
            Projectile.tileCollide = true;
            Projectile.penetrate = 30;
            Projectile.timeLeft = 120;
            Projectile.light = 0.75f;
            Projectile.extraUpdates = 1;
            Projectile.ignoreWater = true;
            Projectile.alpha = 255;
        }

        public override void AI()
        {
            if (Projectile.alpha > 0 ){
                Projectile.alpha -= 10;
            }
            Vector2 mousePosition = Main.MouseWorld;

            Projectile.rotation = Projectile.velocity.ToRotation();
            
        // Lighting on projectile
            Lighting.AddLight(Projectile.Center, 0.2f, 0.25f, 0.25f);
        // Dust effect on projectile
            Dust.NewDust(Projectile.position, Projectile.width, Projectile.height, DustID.Electric, Projectile.velocity.X * 0.25f, Projectile.velocity.Y * 0.25f, 150, default(Color), 0.7f );
        }

    }
}