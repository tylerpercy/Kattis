#include <iostream>

using namespace std;

class Pokemon {
  
public:
    int attack;
    int defense;
    int health;
};

int main()
{
    vector<Pokemon> team;
 
    int n, k;
    cin >> n >> k;
    
    int att, def, hp;
    for (int i = 0; i < n; i++)
    {
        cin >> att, def, hp;
        vector.push(new Pokemon(att, def, hp));
    }
    
    int BestAtt = 0, BestDef = 0, BestHp = 0;
    for (Pokemon p : team)
    {
        
    }
    
    return 0;
}
