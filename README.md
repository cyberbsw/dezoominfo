# dezoominfo

Parses employee information from zoominfo.com.

### Usage

```text
usage: dezoominfo.py [-h] --url URL --pages PAGES --domain DOMAIN [--output OUTPUT]

Dezoominfo scrapes employee information from zoominfo.com

optional arguments:
  -h, --help       show this help message and exit
  --url URL        set url to scrape (https://www.zoominfo.com/pic/COMPANY/NUMBER)
  --pages PAGES    set number of pages to scrape.
  --domain DOMAIN  set domain to use for output formatting.
  --output OUTPUT  set format to output f,F,l,L,D,T [F,L,T,fL@D]
```

### Install

```bash
# install dependecies
apt-get install python python-virtualenv xvfb

# install geckodriver
cd /tmp
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xf geckodriver-v0.24.0-linux64.tar.gz
mv geckodriver /usr/local/sbin/

# install virtual environment
git clone https://github.com/cyberbsw/dezoominfo
cd dezoominfo
virtualenv env
source env/bin/activate
pip install -r requirements.txt

```

### Examples

```bash
python3 dezoominfo.py \
    --url "https://www.zoominfo.com/pic/microsoft-corporation/24904409" \
    --domain microsoft.com \
    --pages 1 \
    --output "F,L,T,fL@D" \
    | column -s, -t | sort

```

```text

Alex      Belotserkovskiy  Cloud Solution Architect                                         ABelotserkovskiy@microsoft.com
Alexia    Moore            Senior Customer Success Manager                                  AMoore@microsoft.com
Anand     Rathi            Service Engineer II                                              ARathi@microsoft.com
Craig     Antwerp          Director - Technology Strategist                                 CAntwerp@microsoft.com
Dexter    Pizzey           Community Development Specialist                                 DPizzey@microsoft.com
Gilles    Dulst            Cloud Specialist                                                 GDulst@microsoft.com
Giovanna  Cirosi           Recruiter                                                        GCirosi@microsoft.com
Kapil     Kochar           Sales Manager                                                    KKochar@microsoft.com
Karen     Peck             Senior Sub Pmm                                                   KPeck@microsoft.com
Karon     Weber            Partner Director                                                 KWeber@microsoft.com
Lucas     Joppa            Chief Environmental Officer                                      LJoppa@microsoft.com
Melanie   McCracken        Global Manager Marketing Communications Advertising & Media      MMcCracken@microsoft.com
Michelle  Huenink          Senior Program Manager Customer Service & Support                MHuenink@microsoft.com
Molly     Whitten          Senior Manager Talent Acquisition                                MWhitten@microsoft.com
Neha      Garg             Senior Product Manager                                           NGarg@microsoft.com
Nikola    Letic            Senior Software Engineer                                         NLetic@microsoft.com
Pedro     Gutierrez        Business & Marketing Category Lead for Music Movies & TV         PGutierrez@microsoft.com
Rae       Niro             Business Msa Administrator                                       RNiro@microsoft.com
Shelly    Park             Sales Manager                                                    SPark@microsoft.com
Shikha    Narwania         Tech Solutions Professor                                         SNarwania@microsoft.com
Sze       Lim              Partner Marketing Advisor                                        SLim@microsoft.com
Tomas     Zunino           Manager Cloud & Enterprise Product Marketing (Microsoft Canada)  TZunino@microsoft.com
Varun     Tiwari           Solution Specialist                                              VTiwari@microsoft.com
Yogita    Kasaven          Program Manager Business                                         YKasaven@microsoft.com
Yvonne    Meng             Sales Manager                                                    YMeng@microsoft.com

```
