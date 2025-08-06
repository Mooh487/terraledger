import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Leaf, Award, TrendingUp, Download, Share2, MapPin } from "lucide-react";

const Dashboard = () => {
  const userStats = {
    totalCredits: 47.5,
    totalOffset: 95000, // kg CO2
    activeProjects: 8,
    retiredCredits: 23.2
  };

  const ownedCredits = [
    {
      id: 1,
      project: "Kenyan Agroforestry Project",
      credits: 12.5,
      purchaseDate: "2024-01-15",
      status: "Active",
      currentValue: 156.25,
      offset: 25000
    },
    {
      id: 2,
      project: "Nigerian Mangrove Restoration",
      credits: 8.3,
      purchaseDate: "2024-02-10",
      status: "Active",
      currentValue: 155.63,
      offset: 16600
    },
    {
      id: 3,
      project: "Ethiopian Highland Reforestation",
      credits: 15.2,
      purchaseDate: "2024-01-28",
      status: "Active",
      currentValue: 232.56,
      offset: 30400
    },
    {
      id: 4,
      project: "Ghanaian Cocoa Agroforestry",
      credits: 11.5,
      purchaseDate: "2024-02-20",
      status: "Retired",
      currentValue: 163.30,
      offset: 23000
    }
  ];

  const achievements = [
    { title: "Climate Champion", description: "Offset 50+ tons CO₂", unlocked: true },
    { title: "Forest Guardian", description: "Support 5+ reforestation projects", unlocked: true },
    { title: "Community Builder", description: "Impact 100+ families", unlocked: true },
    { title: "Carbon Neutral", description: "Offset 100 tons CO₂", unlocked: false },
  ];

  return (
    <div className="min-h-screen bg-background py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-foreground mb-2">My Carbon Dashboard</h1>
          <p className="text-muted-foreground">Track your carbon credits, environmental impact, and achievements</p>
        </div>

        {/* Stats Overview */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card className="border-0 shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Credits Owned</CardTitle>
              <Leaf className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-primary">{userStats.totalCredits}</div>
              <p className="text-xs text-muted-foreground">
                +2.3 credits this month
              </p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">CO₂ Offset</CardTitle>
              <TrendingUp className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-success">{(userStats.totalOffset / 1000).toFixed(1)}t</div>
              <p className="text-xs text-muted-foreground">
                Total CO₂ equivalent offset
              </p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Active Projects</CardTitle>
              <MapPin className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-accent">{userStats.activeProjects}</div>
              <p className="text-xs text-muted-foreground">
                Supporting communities
              </p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Retired Credits</CardTitle>
              <Award className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-warning">{userStats.retiredCredits}</div>
              <p className="text-xs text-muted-foreground">
                Permanently offset
              </p>
            </CardContent>
          </Card>
        </div>

        <Tabs defaultValue="credits" className="space-y-6">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="credits">My Credits</TabsTrigger>
            <TabsTrigger value="impact">Impact Report</TabsTrigger>
            <TabsTrigger value="achievements">Achievements</TabsTrigger>
          </TabsList>

          <TabsContent value="credits" className="space-y-6">
            <div className="grid gap-6">
              {ownedCredits.map((credit) => (
                <Card key={credit.id} className="border-0 shadow-soft">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div>
                        <CardTitle className="text-lg">{credit.project}</CardTitle>
                        <CardDescription>
                          Purchased {credit.credits} credits on {credit.purchaseDate}
                        </CardDescription>
                      </div>
                      <Badge variant={credit.status === "Active" ? "default" : "secondary"}>
                        {credit.status}
                      </Badge>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                      <div>
                        <div className="text-sm text-muted-foreground">Credits Owned</div>
                        <div className="text-lg font-semibold">{credit.credits}</div>
                      </div>
                      <div>
                        <div className="text-sm text-muted-foreground">Current Value</div>
                        <div className="text-lg font-semibold text-success">${credit.currentValue}</div>
                      </div>
                      <div>
                        <div className="text-sm text-muted-foreground">CO₂ Offset</div>
                        <div className="text-lg font-semibold text-primary">{(credit.offset / 1000).toFixed(1)}t</div>
                      </div>
                      <div className="flex gap-2">
                        <Button variant="outline" size="sm">
                          <Download className="h-4 w-4 mr-2" />
                          Certificate
                        </Button>
                        {credit.status === "Active" && (
                          <Button variant="hero" size="sm">
                            Retire
                          </Button>
                        )}
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="impact" className="space-y-6">
            <div className="grid md:grid-cols-2 gap-6">
              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle>Environmental Impact</CardTitle>
                  <CardDescription>Your contribution to fighting climate change</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="space-y-2">
                    <div className="flex justify-between text-sm">
                      <span>CO₂ Offset Progress</span>
                      <span>95t / 100t</span>
                    </div>
                    <Progress value={95} className="h-3" />
                  </div>
                  
                  <div className="grid grid-cols-2 gap-4 pt-4">
                    <div className="text-center p-4 bg-muted rounded-lg">
                      <div className="text-2xl font-bold text-primary">1,240</div>
                      <div className="text-sm text-muted-foreground">Trees Equivalent</div>
                    </div>
                    <div className="text-center p-4 bg-muted rounded-lg">
                      <div className="text-2xl font-bold text-success">8,200</div>
                      <div className="text-sm text-muted-foreground">Miles Not Driven</div>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-soft">
                <CardHeader>
                  <CardTitle>Community Impact</CardTitle>
                  <CardDescription>Supporting local communities across Africa</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div className="grid grid-cols-1 gap-4">
                    <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                      <span className="text-sm">Families Supported</span>
                      <span className="font-semibold text-primary">127</span>
                    </div>
                    <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                      <span className="text-sm">Hectares Restored</span>
                      <span className="font-semibold text-success">43.2</span>
                    </div>
                    <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                      <span className="text-sm">Countries Impacted</span>
                      <span className="font-semibold text-accent">4</span>
                    </div>
                  </div>
                  
                  <Button variant="outline" className="w-full">
                    <Share2 className="h-4 w-4 mr-2" />
                    Share Impact Report
                  </Button>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="achievements" className="space-y-6">
            <div className="grid md:grid-cols-2 gap-6">
              {achievements.map((achievement, index) => (
                <Card key={index} className={`border-0 shadow-soft ${achievement.unlocked ? 'bg-gradient-to-r from-success/10 to-primary/10' : 'opacity-60'}`}>
                  <CardHeader>
                    <div className="flex items-center gap-4">
                      <div className={`w-12 h-12 rounded-full flex items-center justify-center ${
                        achievement.unlocked ? 'bg-gradient-forest' : 'bg-muted'
                      }`}>
                        <Award className={`h-6 w-6 ${achievement.unlocked ? 'text-white' : 'text-muted-foreground'}`} />
                      </div>
                      <div>
                        <CardTitle className={`text-lg ${achievement.unlocked ? 'text-foreground' : 'text-muted-foreground'}`}>
                          {achievement.title}
                        </CardTitle>
                        <CardDescription>{achievement.description}</CardDescription>
                      </div>
                    </div>
                  </CardHeader>
                </Card>
              ))}
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default Dashboard;