
# REST API hosted using SciSpacy for Entity Linkage

## Run locally

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pranav-pitale/nlp-rest-api.git

# Create virtual env
$ python3 venv env
$ source env/bin/activate
$ cd src

# Install dependencies
$ pip install -r requirements.txt


# Run the app
$ python wsgi.py

```

## Run locally using web server

```bash

# Start webserver
$ gunicorn --bind 0.0.0.0:5000 wsgi:app --timeout 3600

```
## Run locally using Docker

Install docker on your machine

```bash
$ cd src

# Build Docker Image
$ docker build .

# Build Docker Image
$ docker run -p 8000:8000 -i -t IMAGE_ID

```

## Entity enpoint

```GET
http://0.0.0.0:5000/api/Entities?text=Spinal and bulbar muscular atrophy 
```
```
{
    "Entities": [
        {
            "cui": "C1947952",
            "name": "anatomical bulb",
            "definition": "A rounded dilation or expansion in a canal, vessel, or organ.",
            "aliases": [
                "Bulbar",
                "Bulb"
            ]
        },
        {
            "cui": "C0032372",
            "name": "Poliomyelitis, Bulbar",
            "definition": "A form of paralytic poliomyelitis affecting neurons of the MEDULLA OBLONGATA of the brain stem. Clinical features include impaired respiration, HYPERTENSION, alterations of vasomotor control, and dysphagia. Weakness and atrophy of the limbs and trunk due to spinal cord involvement is usually associated. (From Adams et al., Principles of Neurology, 6th ed, p765)",
            "aliases": [
                "Acute bulbar polioencephalitis",
                "Bulbar Polio",
                "Poliomyelitis, Medullary Involvement",
                "BULBAR POLIO",
                "Acute paralytic poliomyelitis specified as bulbar",
                "Polio, Bulbar",
                "Bulbar Poliomyelitis",
                "Anterior acute poliomyelitis",
                "Acute infantile paralysis",
                "Acute paralytic poliomyelitis, bulbar",
                "bulbar poliomyelitis",
                "POLIOMYELITIS, ANTERIOR, ACUTE",
                "bulbar polio",
                "Acute anterior poliomyelitis",
                "Anterior acute poliomyelitis (disorder)",
                "Medullary Involvement Poliomyelitis",
                "acute anterior poliomyelitis",
                "Acute paralytic poliomyelitis, bulbar (disorder)",
                "Poliomyelitis specified as bulbar",
                "Acute anterior bulbar polioencephalomyelitis",
                "POLIOMYELITIS, PARALYTIC, BULBAR",
                "Anterior acute poliomyelitis, NOS",
                "Acute paralytic bulbar poliomyelitis"
            ]
        },
        {
            "cui": "C2586323",
            "name": "Structure of fascial sheath of eyeball",
            "definition": "Sheath of the eyeball consisting of fascia extending from the OPTIC NERVE to the corneal limbus.",
            "aliases": [
                "Eyeball, sheath",
                "Vaginal bulbi",
                "Capsule, Tenon",
                "Bulbar sheath",
                "Tenon's capsule",
                "Fascia bulbi",
                "Tenons Capsule",
                "Structure of fascial sheath of eyeball",
                "tenon capsule",
                "Sheath of eyeball",
                "Substantia Propria",
                "Structure of fascial sheath of eyeball (body structure)",
                "Capsule, Tenon's",
                "Capsule of Tenon",
                "Tenon Capsule",
                "Tenon's Capsule",
                "tenon's capsule",
                "capsule of tenon",
                "Tenon's capsule structure",
                "Fascial sheath of eyeball"
            ]
        },
        {
            "cui": "C1744560",
            "name": "Bulbar urethra",
            "definition": "The portion of the penile urethra that spans the bulb of the penis.",
            "aliases": [
                "Structure of bulbar urethra",
                "Bulbar urethra",
                "Bulbar Portion of the Urethra",
                "Structure of bulbar urethra (body structure)",
                "Bulbar Urethra"
            ]
        },
        {
            "cui": "C0030442",
            "name": "Progressive bulbar palsy",
            "definition": "A motor neuron disease marked by progressive weakness of the muscles innervated by cranial nerves of the lower brain stem. Clinical manifestations include dysarthria, dysphagia, facial weakness, tongue weakness, and fasciculations of the tongue and facial muscles. The adult form of the disease is marked initially by bulbar weakness which progresses to involve motor neurons throughout the neuroaxis. Eventually this condition may become indistinguishable from AMYOTROPHIC LATERAL SCLEROSIS. Fazio-Londe syndrome is an inherited form of this illness which occurs in children and young adults. (Adams et al., Principles of Neurology, 6th ed, p1091; Brain 1992 Dec;115(Pt 6):1889-1900)",
            "aliases": [
                "bulbar palsy progressive",
                "Palsies, Progressive Bulbar",
                "Progressive Bulbar Palsy",
                "Bulbar Palsy, Progressive",
                "Progressive bulbar palsy (disorder)",
                "PBP - Progressive bulbar palsy",
                "Bulbar paralysis",
                "Progressive Bulbar Palsies",
                "Bulbar palsy",
                "Progressive bulbar palsy",
                "Palsy, Progressive Bulbar",
                "Bulbar Palsies, Progressive",
                "progressive bulbar palsy"
            ]
        }
    ]
}
```
