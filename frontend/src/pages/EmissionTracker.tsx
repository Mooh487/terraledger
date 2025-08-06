import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { Flame, Zap, Car, Trash2, Calculator, TrendingDown, Lightbulb } from "lucide-react";

const EmissionTracker = () => {
  const [cookingFuel, setCookingFuel] = useState("");
  const [fuelAmount, setFuelAmount] = useState("");
  const [generatorHours, setGeneratorHours] = useState("");
  const [wasteAmount, setWasteAmount] = useState("");

  const monthlyEmissions = {
    cooking: 45, // kg CO2
    electricity: 32,
    transport: 28,
    waste: 15
  };

  const totalEmissions = Object.values(monthlyEmissions).reduce((a, b) => a + b, 0);
  const yearlyEmissions = totalEmissions * 12;

  const recommendations = [
    {
      activity: "Switch to LPG for cooking",
      reduction: "40% cooking emissions",
      savings: "18 kg CO₂/month",
      difficulty: "Medium"
    },
    {
      activity: "Use solar lights instead of generator",
      reduction: "60% electricity emissions",
      savings: "19 kg CO₂/month",
      difficulty: "Easy"
    },
    {
      activity: "Composting organic waste",
      reduction: "70% waste emissions",
      savings: "10 kg CO₂/month",
      difficulty: "Easy"
    },
    {
      activity: "Use public transport 2x/week",
      reduction: "30% transport emissions",
      savings: "8 kg CO₂/month",
      difficulty: "Easy"
    }
  ];

  return (
    <div className="min-h-screen bg-background py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-foreground mb-6">
            Domestic Emission Tracker
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Track your household's carbon footprint and discover practical ways to reduce emissions 
            while supporting your community's environmental goals.
          </p>
        </div>

        <Tabs defaultValue="calculator" className="space-y-8">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="calculator">Calculate Emissions</TabsTrigger>
            <TabsTrigger value="tracker">Monthly Tracker</TabsTrigger>
            <TabsTrigger value="recommendations">Recommendations</TabsTrigger>
          </TabsList>

          <TabsContent value="calculator" className="space-y-8">
            <div className="grid md:grid-cols-2 gap-8">
              {/* Input Form */}
              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Calculator className="h-5 w-5" />
                    Household Activities
                  </CardTitle>
                  <CardDescription>
                    Enter your weekly household activities to calculate emissions
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  {/* Cooking */}
                  <div className="space-y-3">
                    <Label className="flex items-center gap-2">
                      <Flame className="h-4 w-4" />
                      Cooking Fuel Type
                    </Label>
                    <Select value={cookingFuel} onValueChange={setCookingFuel}>
                      <SelectTrigger>
                        <SelectValue placeholder="Select cooking fuel" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="charcoal">Charcoal</SelectItem>
                        <SelectItem value="firewood">Firewood</SelectItem>
                        <SelectItem value="kerosene">Kerosene</SelectItem>
                        <SelectItem value="lpg">LPG Gas</SelectItem>
                        <SelectItem value="electric">Electric</SelectItem>
                      </SelectContent>
                    </Select>
                    <div className="grid grid-cols-2 gap-2">
                      <div>
                        <Label className="text-sm">Amount per week (kg)</Label>
                        <Input 
                          type="number" 
                          value={fuelAmount}
                          onChange={(e) => setFuelAmount(e.target.value)}
                          placeholder="0"
                        />
                      </div>
                    </div>
                  </div>

                  {/* Generator */}
                  <div className="space-y-3">
                    <Label className="flex items-center gap-2">
                      <Zap className="h-4 w-4" />
                      Generator Usage
                    </Label>
                    <div className="grid grid-cols-2 gap-2">
                      <div>
                        <Label className="text-sm">Hours per week</Label>
                        <Input 
                          type="number"
                          value={generatorHours}
                          onChange={(e) => setGeneratorHours(e.target.value)}
                          placeholder="0"
                        />
                      </div>
                    </div>
                  </div>

                  {/* Waste */}
                  <div className="space-y-3">
                    <Label className="flex items-center gap-2">
                      <Trash2 className="h-4 w-4" />
                      Waste Burning
                    </Label>
                    <div className="grid grid-cols-2 gap-2">
                      <div>
                        <Label className="text-sm">Waste burned (kg/week)</Label>
                        <Input 
                          type="number"
                          value={wasteAmount}
                          onChange={(e) => setWasteAmount(e.target.value)}
                          placeholder="0"
                        />
                      </div>
                    </div>
                  </div>

                  <Button variant="hero" className="w-full">
                    Calculate Emissions
                  </Button>
                </CardContent>
              </Card>

              {/* Results */}
              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle>Your Carbon Footprint</CardTitle>
                  <CardDescription>
                    Monthly emissions breakdown for your household
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="text-center p-6 bg-gradient-to-r from-primary/10 to-accent/10 rounded-lg">
                    <div className="text-3xl font-bold text-primary">{totalEmissions} kg</div>
                    <div className="text-muted-foreground">CO₂ per month</div>
                    <div className="text-lg font-semibold text-accent mt-2">{(yearlyEmissions / 1000).toFixed(1)} tons/year</div>
                  </div>

                  <div className="space-y-4">
                    {Object.entries(monthlyEmissions).map(([category, amount]) => (
                      <div key={category} className="space-y-2">
                        <div className="flex justify-between text-sm">
                          <span className="capitalize">{category}</span>
                          <span className="font-medium">{amount} kg CO₂</span>
                        </div>
                        <Progress value={(amount / totalEmissions) * 100} className="h-2" />
                      </div>
                    ))}
                  </div>

                  <div className="p-4 bg-warning/10 rounded-lg">
                    <div className="flex items-center gap-2 mb-2">
                      <Lightbulb className="h-4 w-4 text-warning" />
                      <span className="font-medium">Impact Context</span>
                    </div>
                    <p className="text-sm text-muted-foreground">
                      Your annual emissions could be offset by purchasing {(yearlyEmissions / 2000).toFixed(1)} carbon credits 
                      from our marketplace, supporting local reforestation projects.
                    </p>
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="tracker" className="space-y-8">
            <div className="grid md:grid-cols-3 gap-6">
              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle className="text-lg">This Month</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-primary">{totalEmissions} kg</div>
                  <p className="text-sm text-muted-foreground">CO₂ emissions</p>
                  <div className="mt-4 space-y-2">
                    <div className="flex justify-between text-sm">
                      <span>Monthly Goal</span>
                      <span>100 kg</span>
                    </div>
                    <Progress value={(totalEmissions / 100) * 100} className="h-2" />
                  </div>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle className="text-lg">Vs Last Month</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex items-center gap-2">
                    <TrendingDown className="h-5 w-5 text-success" />
                    <div className="text-2xl font-bold text-success">-12%</div>
                  </div>
                  <p className="text-sm text-muted-foreground">15 kg CO₂ reduction</p>
                  <Badge variant="outline" className="mt-2 text-success border-success">
                    Great progress!
                  </Badge>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle className="text-lg">Annual Target</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-accent">{(yearlyEmissions / 1000).toFixed(1)}t</div>
                  <p className="text-sm text-muted-foreground">Projected yearly</p>
                  <div className="mt-4 space-y-2">
                    <div className="flex justify-between text-sm">
                      <span>Target: 1.0t</span>
                      <span>{((yearlyEmissions / 1000) / 1.0 * 100).toFixed(0)}%</span>
                    </div>
                    <Progress value={((yearlyEmissions / 1000) / 1.0) * 100} className="h-2" />
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="recommendations" className="space-y-8">
            <div className="grid gap-6">
              {recommendations.map((rec, index) => (
                <Card key={index} className="border-0 shadow-soft hover:shadow-glow transition-all duration-300">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div>
                        <CardTitle className="text-lg">{rec.activity}</CardTitle>
                        <CardDescription>Potential reduction: {rec.reduction}</CardDescription>
                      </div>
                      <Badge variant={rec.difficulty === "Easy" ? "default" : "secondary"}>
                        {rec.difficulty}
                      </Badge>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center justify-between">
                      <div className="text-sm text-muted-foreground">
                        <span className="font-medium text-success">{rec.savings}</span> saved monthly
                      </div>
                      <Button variant="outline">Learn More</Button>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            <Card className="border-0 shadow-soft bg-gradient-to-r from-primary/5 to-accent/5">
              <CardHeader>
                <CardTitle>Carbon Offset Opportunity</CardTitle>
                <CardDescription>
                  Offset your remaining emissions while supporting African communities
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground mb-2">
                      After implementing recommendations, offset remaining {((yearlyEmissions * 0.4) / 1000).toFixed(1)} tons/year
                    </p>
                    <p className="font-medium">
                      Estimated cost: ${((yearlyEmissions * 0.4) / 1000 * 15).toFixed(0)}/year
                    </p>
                  </div>
                  <Button variant="hero">
                    Browse Credits
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default EmissionTracker;