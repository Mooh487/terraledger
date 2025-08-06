import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { MapPin, Leaf, TrendingUp, Star, Filter, Search } from "lucide-react";
import { Input } from "@/components/ui/input";

// Import local images
import kenyanAgroforestryImg from "@/assets/kenyan-agroforestry.jpg";
import nigerianMangroveImg from "@/assets/nigerian-mangrove.jpg";
import ethiopianHighlandImg from "@/assets/ethiopian-highland.jpg";
import ghanaianCocoaImg from "@/assets/ghanaian-cocoa.jpg";

const Marketplace = () => {
  const [selectedFilter, setSelectedFilter] = useState("all");

  const carbonCredits = [
    {
      id: 1,
      name: "Kenyan Agroforestry Project",
      location: "Nakuru County, Kenya",
      type: "Agroforestry",
      price: 12.50,
      totalCredits: 1000,
      availableCredits: 750,
      sequestrationRate: 85,
      verification: "AI + Satellite",
      rating: 4.9,
      image: kenyanAgroforestryImg,
      impact: "Supporting 200 farming families while restoring degraded land"
    },
    {
      id: 2,
      name: "Nigerian Mangrove Restoration",
      location: "Niger Delta, Nigeria",
      type: "Coastal Restoration",
      price: 18.75,
      totalCredits: 500,
      availableCredits: 320,
      sequestrationRate: 92,
      verification: "AI + Satellite",
      rating: 4.8,
      image: nigerianMangroveImg,
      impact: "Protecting coastal communities and biodiversity"
    },
    {
      id: 3,
      name: "Ethiopian Highland Reforestation",
      location: "Amhara Region, Ethiopia",
      type: "Reforestation",
      price: 15.30,
      totalCredits: 2000,
      availableCredits: 1650,
      sequestrationRate: 78,
      verification: "AI + Satellite",
      rating: 4.7,
      image: ethiopianHighlandImg,
      impact: "Restoring traditional forest landscapes and water sources"
    },
    {
      id: 4,
      name: "Ghanaian Cocoa Agroforestry",
      location: "Ashanti Region, Ghana",
      type: "Agroforestry",
      price: 14.20,
      totalCredits: 800,
      availableCredits: 480,
      sequestrationRate: 89,
      verification: "AI + Satellite",
      rating: 4.9,
      image: ghanaianCocoaImg,
      impact: "Improving cocoa farmer livelihoods through sustainable practices"
    }
  ];

  const filteredCredits = selectedFilter === "all" 
    ? carbonCredits 
    : carbonCredits.filter(credit => credit.type.toLowerCase().includes(selectedFilter.toLowerCase()));

  return (
    <div className="min-h-screen bg-background py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-foreground mb-6">
            Carbon Credit Marketplace
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Discover verified, high-impact carbon credits from across Africa. 
            Every purchase directly supports local communities and environmental restoration.
          </p>
        </div>

        {/* Search and Filters */}
        <div className="mb-8">
          <Tabs value={selectedFilter} onValueChange={setSelectedFilter} className="w-full">
            <div className="flex flex-col md:flex-row gap-4 items-center justify-between">
              <div className="flex-1 max-w-md">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground h-4 w-4" />
                  <Input 
                    placeholder="Search projects by name or location..." 
                    className="pl-10"
                  />
                </div>
              </div>
              
              <TabsList className="grid w-full md:w-auto grid-cols-4 lg:grid-cols-4">
                <TabsTrigger value="all">All Projects</TabsTrigger>
                <TabsTrigger value="agroforestry">Agroforestry</TabsTrigger>
                <TabsTrigger value="reforestation">Reforestation</TabsTrigger>
                <TabsTrigger value="coastal">Coastal</TabsTrigger>
              </TabsList>
            </div>
            
            {/* Statistics */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 p-6 bg-card rounded-lg shadow-soft">
              <div className="text-center">
                <div className="text-2xl font-bold text-primary">{filteredCredits.length}</div>
                <div className="text-sm text-muted-foreground">Active Projects</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-success">
                  {filteredCredits.reduce((acc, credit) => acc + credit.availableCredits, 0).toLocaleString()}
                </div>
                <div className="text-sm text-muted-foreground">Credits Available</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-accent">
                  ${filteredCredits.reduce((acc, credit) => acc + (credit.price * credit.availableCredits), 0).toLocaleString()}
                </div>
                <div className="text-sm text-muted-foreground">Total Value</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-warning">4.8★</div>
                <div className="text-sm text-muted-foreground">Avg. Rating</div>
              </div>
            </div>
          </Tabs>
        </div>

        {/* Credits Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredCredits.map((credit) => (
            <Card key={credit.id} className="overflow-hidden border-0 shadow-soft hover:shadow-glow transition-all duration-300 hover:-translate-y-2">
              <div className="relative h-48 overflow-hidden">
                <img 
                  src={credit.image} 
                  alt={credit.name}
                  className="w-full h-full object-cover transition-transform duration-300 hover:scale-110"
                />
                <div className="absolute top-4 left-4">
                  <Badge variant="secondary" className="bg-white/90 text-primary">
                    {credit.type}
                  </Badge>
                </div>
                <div className="absolute top-4 right-4">
                  <Badge variant="outline" className="bg-white/90 text-warning border-warning">
                    <Star className="w-3 h-3 mr-1 fill-current" />
                    {credit.rating}
                  </Badge>
                </div>
              </div>
              
              <CardHeader>
                <CardTitle className="flex items-start justify-between">
                  <span className="text-lg">{credit.name}</span>
                  <div className="text-right">
                    <div className="text-2xl font-bold text-primary">${credit.price}</div>
                    <div className="text-sm text-muted-foreground">per credit</div>
                  </div>
                </CardTitle>
                
                <CardDescription className="flex items-center text-base">
                  <MapPin className="w-4 h-4 mr-2" />
                  {credit.location}
                </CardDescription>
              </CardHeader>
              
              <CardContent className="space-y-4">
                <p className="text-sm text-muted-foreground">{credit.impact}</p>
                
                <div className="space-y-3">
                  <div className="flex justify-between text-sm">
                    <span>Sequestration Progress</span>
                    <span className="font-medium">{credit.sequestrationRate}%</span>
                  </div>
                  <Progress value={credit.sequestrationRate} className="h-2" />
                  
                  <div className="flex justify-between text-sm">
                    <span>Available Credits</span>
                    <span className="font-medium">
                      {credit.availableCredits.toLocaleString()} / {credit.totalCredits.toLocaleString()}
                    </span>
                  </div>
                  <Progress 
                    value={(credit.availableCredits / credit.totalCredits) * 100} 
                    className="h-2"
                  />
                </div>
                
                <div className="flex items-center justify-between pt-2">
                  <Badge variant="outline" className="text-xs">
                    <Leaf className="w-3 h-3 mr-1" />
                    {credit.verification}
                  </Badge>
                  <Badge variant="outline" className="text-xs">
                    <TrendingUp className="w-3 h-3 mr-1" />
                    Live Monitoring
                  </Badge>
                </div>
                
                <div className="flex gap-2 pt-4">
                  <Button variant="hero" className="flex-1">
                    Buy Credits
                  </Button>
                  <Button variant="outline" size="icon">
                    <MapPin className="h-4 w-4" />
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Load More */}
        <div className="text-center mt-12">
          <Button variant="outline" size="lg">
            Load More Projects
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Marketplace;