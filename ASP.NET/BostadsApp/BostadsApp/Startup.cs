using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(BostadsApp.Startup))]
namespace BostadsApp
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
