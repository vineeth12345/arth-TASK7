FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build-env

WORKDIR /app

COPY GrandNode.sln .
COPY Grand.Domain/Grand.Domain.csproj Grand.Domain/Grand.Domain.csproj
COPY Grand.Core/Grand.Core.csproj Grand.Core/Grand.Core.csproj
COPY Grand.Framework/Grand.Framework.csproj Grand.Framework/Grand.Framework.csproj
COPY Grand.Services/Grand.Services.csproj Grand.Services/Grand.Services.csproj
COPY Grand.Web/Grand.Web.csproj Grand.Web/Grand.Web.csproj
COPY Plugins/Grand.Plugin.DiscountRequirements.Standard/Grand.Plugin.DiscountRequirements.Standard.csproj Plugins/Grand.Plugin.DiscountRequirements.Standard/Grand.Plugin.DiscountRequirements.Standard.csproj
COPY Plugins/Grand.Plugin.ExchangeRate.McExchange/Grand.Plugin.ExchangeRate.McExchange.csproj Plugins/Grand.Plugin.ExchangeRate.McExchange/Grand.Plugin.ExchangeRate.McExchange.csproj
COPY Plugins/Grand.Plugin.ExternalAuth.Facebook/Grand.Plugin.ExternalAuth.Facebook.csproj Plugins/Grand.Plugin.ExternalAuth.Facebook/Grand.Plugin.ExternalAuth.Facebook.csproj
COPY Plugins/Grand.Plugin.ExternalAuth.Google/Grand.Plugin.ExternalAuth.Google.csproj Plugins/Grand.Plugin.ExternalAuth.Google/Grand.Plugin.ExternalAuth.Google.csproj
COPY Plugins/Grand.Plugin.Payments.BrainTree/Grand.Plugin.Payments.BrainTree.csproj Plugins/Grand.Plugin.Payments.BrainTree/Grand.Plugin.Payments.BrainTree.csproj
COPY Plugins/Grand.Plugin.Payments.CashOnDelivery/Grand.Plugin.Payments.CashOnDelivery.csproj Plugins/Grand.Plugin.Payments.CashOnDelivery/Grand.Plugin.Payments.CashOnDelivery.csproj
COPY Plugins/Grand.Plugin.Payments.PayPalStandard/Grand.Plugin.Payments.PayPalStandard.csproj Plugins/Grand.Plugin.Payments.PayPalStandard/Grand.Plugin.Payments.PayPalStandard.csproj
COPY Plugins/Grand.Plugin.Shipping.ByWeight/Grand.Plugin.Shipping.ByWeight.csproj Plugins/Grand.Plugin.Shipping.ByWeight/Grand.Plugin.Shipping.ByWeight.csproj
COPY Plugins/Grand.Plugin.Shipping.FixedRateShipping/Grand.Plugin.Shipping.FixedRateShipping.csproj Plugins/Grand.Plugin.Shipping.FixedRateShipping/Grand.Plugin.Shipping.FixedRateShipping.csproj
COPY Plugins/Grand.Plugin.Shipping.ShippingPoint/Grand.Plugin.Shipping.ShippingPoint.csproj Plugins/Grand.Plugin.Shipping.ShippingPoint/Grand.Plugin.Shipping.ShippingPoint.csproj
COPY Plugins/Grand.Plugin.Tax.CountryStateZip/Grand.Plugin.Tax.CountryStateZip.csproj Plugins/Grand.Plugin.Tax.CountryStateZip/Grand.Plugin.Tax.CountryStateZip.csproj
COPY Plugins/Grand.Plugin.Tax.FixedRate/Grand.Plugin.Tax.FixedRate.csproj Plugins/Grand.Plugin.Tax.FixedRate/Grand.Plugin.Tax.FixedRate.csproj
COPY Plugins/Grand.Plugin.Widgets.GoogleAnalytics/Grand.Plugin.Widgets.GoogleAnalytics.csproj Plugins/Grand.Plugin.Widgets.GoogleAnalytics/Grand.Plugin.Widgets.GoogleAnalytics.csproj
COPY Plugins/Grand.Plugin.Widgets.FacebookPixel/Grand.Plugin.Widgets.FacebookPixel.csproj Plugins/Grand.Plugin.Widgets.FacebookPixel/Grand.Plugin.Widgets.FacebookPixel.csproj
COPY Plugins/Grand.Plugin.Widgets.Slider/Grand.Plugin.Widgets.Slider.csproj Plugins/Grand.Plugin.Widgets.Slider/Grand.Plugin.Widgets.Slider.csproj

# Copy everything else and build
COPY . ./
RUN dotnet publish Grand.Web -c Release -o out
RUN dotnet build Plugins/Grand.Plugin.DiscountRequirements.Standard
RUN dotnet build Plugins/Grand.Plugin.ExchangeRate.McExchange
RUN dotnet build Plugins/Grand.Plugin.ExternalAuth.Facebook
RUN dotnet build Plugins/Grand.Plugin.ExternalAuth.Google
RUN dotnet build Plugins/Grand.Plugin.Payments.BrainTree
RUN dotnet build Plugins/Grand.Plugin.Payments.CashOnDelivery
RUN dotnet build Plugins/Grand.Plugin.Payments.PayPalStandard
RUN dotnet build Plugins/Grand.Plugin.Shipping.ByWeight
RUN dotnet build Plugins/Grand.Plugin.Shipping.FixedRateShipping
RUN dotnet build Plugins/Grand.Plugin.Shipping.ShippingPoint
RUN dotnet build Plugins/Grand.Plugin.Tax.CountryStateZip
RUN dotnet build Plugins/Grand.Plugin.Tax.FixedRate
RUN dotnet build Plugins/Grand.Plugin.Widgets.GoogleAnalytics
RUN dotnet build Plugins/Grand.Plugin.Widgets.FacebookPixel
RUN dotnet build Plugins/Grand.Plugin.Widgets.Slider

Deleting start line: FROM container.babelstreet.com/synopsys-detect as scanner
Deleting intermediate line: ARG BUILD_ENVIRONMENT="local"
Deleting intermediate line: ARG BRANCH_NAME
Deleting intermediate line: ARG FAIL_ON_SEVERITY_LEVEL
Deleting intermediate line: WORKDIR C:/
Deleting intermediate line: SHELL ["pwsh", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]
Deleting intermediate line: # Make sure to include any new project's .csproj files
Deleting intermediate line: # DON'T include any test project's .csproj files.
Deleting intermediate line: COPY ["DataSorcerer/DataSorcerer.csproj", "/src/"]
Deleting intermediate line: COPY ["BabelStreet.DataSorcerer/BabelStreet.DataSorcerer.csproj", "/src/"]
Deleting intermediate line: ENV detect.project.name="DataSorcerer"
Deleting intermediate line: # Source can be found at https://git.babelstreet.com/projects/DOC/repos/synopsis-detect/browse/scan.ps1
Deleting intermediate line: RUN pwsh -c $(get-content C:\scan.ps1)
Deleting intermediate line: 
Deleting intermediate line: # Build runtime image
Deleting intermediate line: FROM mcr.microsoft.com/dotnet/core/aspnet:3.1.0
Deleting intermediate line: 
Deleting intermediate line: RUN apt-get update -qq && apt-get -y install libgdiplus libc6-dev
Deleting intermediate line: 
Deleting intermediate line: 
Deleting intermediate line: WORKDIR /app
Deleting intermediate line: COPY --from=build-env /app/out/ .
Deleting intermediate line: COPY --from=build-env /app/Grand.Web/Plugins/ ./Plugins/
Deleting intermediate line: 
Deleting intermediate line: VOLUME /app/App_Data /app/wwwroot /app/Plugins /app/Themes
Deleting intermediate line: 
Deleting intermediate line: RUN chmod 755 /app/Rotativa/Linux/wkhtmltopdf
Deleting intermediate line: 
Deleting intermediate line: CMD ["dotnet", "Grand.Web.dll"]
