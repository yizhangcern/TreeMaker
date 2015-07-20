// CMSSW headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

//ROOT headers
#include "TString.h"
#include "TTree.h"
#include <TFile.h>
#include "TLorentzVector.h"
#include "Math/GenVector/LorentzVector.h"

//STL headers
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <sstream>

using namespace std;

//enum with known types
enum TreeTypes { t_bool=0, t_int=1, t_double=2, t_string=3, t_lorentz=4, t_vbool=100, t_vint=101, t_vdouble=102, t_vstring=103, t_vlorentz=104, t_recocand=1000 };

//forward declaration of helper class
class TreeObjectBase;

//
// class declaration
//

class TreeMaker : public edm::EDProducer {
public:
  explicit TreeMaker(const edm::ParameterSet&);
  ~TreeMaker();
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
private:
  virtual void beginJob() override;
  virtual void produce(edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  // ----------member data ---------------------------
  string treeName;
  TTree* tree;	
  bool debug;
  bool doLorentz;
  vector<string> VarTypeNames;
  vector<TreeTypes> VarTypes;
  vector<vector<string> > VarNames;
  map<string,unsigned> nameCache;
  // general event information
  UInt_t runNum;
  UInt_t lumiBlockNum;
  UInt_t evtNum;
  vector<TreeObjectBase*> variables;
};

//helper classes
class TreeObjectBase {
	public:
		//constructor
		TreeObjectBase() : tempFull(""), branchType("") {}
		TreeObjectBase(string tempFull_, TTree* tree_) : tempFull(tempFull_), nameInTree(tempFull_), tagName(tempFull_), tree(tree_) {}
		//destructor
		virtual ~TreeObjectBase() {}
		//functions
		virtual void Initialize(map<string,unsigned>& nameCache) {}
		virtual void AddBranch() {}
		virtual void SetDefault() {}
		virtual void FillTree(edm::Event& iEvent) {}
		
		//common helper function
		virtual void FinalizeName(map<string,unsigned>& nameCache){
			auto nameIt = nameCache.find(nameInTree);
			if(nameIt != nameCache.end()){
				stringstream ss;
				ss << nameInTree << "_" << nameIt->second;
				nameInTree = ss.str();
				cout << "Warning: name in tree already defined, alternating name... " << nameInTree << endl;
				//increment count for this name
				nameIt->second++;
			}
			else {
				//add this name to the cache
				nameCache[nameInTree] = 1;
			}
		}
		
	protected:
		//member variables
		string tempFull, nameInTree, tagName, branchType;
		TTree* tree;
		edm::InputTag tag;
};

template <class T>
class TreeObject : public TreeObjectBase {
	public:
		//constructor
		TreeObject() : TreeObjectBase() {}
		TreeObject(string tempFull_, TTree* tree_) : TreeObjectBase(tempFull_,tree_) {}
		//destructor
		virtual ~TreeObject() {}
		//functions
		virtual void Initialize(map<string,unsigned>& nameCache) {
			//case 1: x      -> tag = x,   name = x
			//case 2: x:y    -> tag = x:y, name = y
			//case 3: x(y)   -> tag = x,   name = y
			//case 4: x:y(z) -> tag = x:y, name = z
			
			size_t pos1 = tempFull.find('(');
			size_t pos2 = tempFull.find(')');
			size_t pos3 = tempFull.find(':');
			
			//case 3/4
			if(pos1!=string::npos && pos2!=string::npos){
				tagName = tempFull.substr(0,pos1);
				nameInTree = tempFull.substr(pos1+1,pos2-(pos1+1));
			}
			//case 2
			else if(pos3!=string::npos){
				nameInTree = tempFull.substr(pos3+1);
			}
			//case 1, nothing to do
			//(constructor assumes this case by default)
			else { }
			
			cout << "full name: " << tempFull << " -> tag: " << tagName << " nameInTree: " << nameInTree << endl;
			//make tag
			tag = edm::InputTag(tagName);
			
			//finalize name to avoid duplicates
			FinalizeName(nameCache);
			
			//add branch to tree
			AddBranch();
		}
		virtual void FillTree(edm::Event& iEvent){
			SetDefault();
			edm::Handle<T> var;
			iEvent.getByLabel(tag,var);
			if( var.isValid() ) {
				value = *var;
			}
			else {
				cout << "WARNING ... " << tagName << " is NOT valid?!" << endl;
			}
		}
		//these will be implemented below for specializations
		virtual void AddBranch() {}
		virtual void SetDefault() {}
		
	protected:
		//member variables
		T value;
};

//specialize!

template<>
void TreeObject<bool>::AddBranch() { tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/O").c_str()); }
template<>
void TreeObject<int>::AddBranch() { tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/I").c_str()); }
template<>
void TreeObject<double>::AddBranch() { tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/F").c_str()); }
template<>
void TreeObject<string>::AddBranch() { tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<TLorentzVector>::AddBranch() { tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObject<vector<bool> >::AddBranch() { tree->Branch(nameInTree.c_str(),"vector<bool>",&value,32000,0); }
template<>
void TreeObject<vector<int> >::AddBranch() { tree->Branch(nameInTree.c_str(),"vector<int>",&value,32000,0); }
template<>
void TreeObject<vector<double> >::AddBranch() { tree->Branch(nameInTree.c_str(),"vector<double>",&value,32000,0); }
template<>
void TreeObject<vector<string> >::AddBranch() { tree->Branch(nameInTree.c_str(),"vector<string>",&value,32000,0); }
template<>
void TreeObject<vector<TLorentzVector> >::AddBranch() { tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0); }

template<>
void TreeObject<bool>::SetDefault() { value = false; }
template<>
void TreeObject<int>::SetDefault() { value = 9999; }
template<>
void TreeObject<double>::SetDefault() { value = 9999.; }
template<>
void TreeObject<string>::SetDefault() { value = ""; }
template<>
void TreeObject<TLorentzVector>::SetDefault() { value.SetXYZT(0,0,0,0); }
template<>
void TreeObject<vector<bool> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<int> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<double> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<string> >::SetDefault() { value.clear(); }
template<>
void TreeObject<vector<TLorentzVector> >::SetDefault() { value.clear(); }

//derived version of vector<TLorentzVector> for RecoCand
//with switch for vector<double> pt, eta, phi, energy instead
class TreeRecoCand : public TreeObject<vector<TLorentzVector> > {
	public:
		//constructor
		TreeRecoCand() : TreeObject<vector<TLorentzVector> >() {}
		TreeRecoCand(string tempFull_, TTree* tree_, bool doLorentz_=true) : TreeObject<vector<TLorentzVector> >(tempFull_,tree_), doLorentz(doLorentz_) {}
		//destructor
		virtual ~TreeRecoCand() {}
		
		//functions
		virtual void FillTree(edm::Event& iEvent){
			SetDefault();
			edm::Handle< edm::View<reco::Candidate> > cands;
			iEvent.getByLabel(tag,cands);
			if( cands.isValid() ) {
				if(doLorentz){
					value.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						value.emplace_back(iPart->px(), iPart->py(), iPart->pz(), iPart->energy());
					}
				}
				else{
					pt.reserve(cands->size());
					eta.reserve(cands->size());
					phi.reserve(cands->size());
					energy.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						pt.emplace_back(iPart->pt());
						eta.emplace_back(iPart->eta());
						phi.emplace_back(iPart->phi());
						energy.emplace_back(iPart->energy());
					}
				}
			}
			else {
				cout << "WARNING ... " << tagName << " is NOT valid?!" << endl;
			}
		}
		virtual void AddBranch() {
			if(doLorentz){
				tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0);
			}
			else {
				tree->Branch((nameInTree+"Pt").c_str(),"vector<double>",&pt,32000,0);
				tree->Branch((nameInTree+"Eta").c_str(),"vector<double>",&eta,32000,0);
				tree->Branch((nameInTree+"Phi").c_str(),"vector<double>",&phi,32000,0);
				tree->Branch((nameInTree+"E").c_str(),"vector<double>",&energy,32000,0);
			}
		}
		virtual void SetDefault() {
			if(doLorentz){
				value.clear();
			}
			else{
				pt.clear();
				eta.clear();
				phi.clear();
				energy.clear();
			}
		}
	
	protected:
		//member variables
		bool doLorentz;
		vector<double> pt, eta, phi, energy;
};