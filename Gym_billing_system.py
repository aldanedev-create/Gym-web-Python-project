# GYM-ON-THE-ROCK BILLING SYSTEM
# Contemporary Programming – Project 1 | UTech | May 13,2026

import datetime

# ── DATA STRUCTURES ───────────────────────────────────────────
instructors = {
    "INS101": {"id":"INS101","first_name":"Marcus", "last_name":"Reid",     "contact":"876-421-7730","specialization":"Spinning"},
    "INS102": {"id":"INS102","first_name":"Alicia", "last_name":"Brown",    "contact":"876-532-9841","specialization":"Martial Arts"},
    "INS103": {"id":"INS103","first_name":"Damion", "last_name":"Campbell", "contact":"876-678-3312","specialization":"Spinning"},
    "INS104": {"id":"INS104","first_name":"Kezia",  "last_name":"Thompson", "contact":"876-799-0045","specialization":"Martial Arts"},
}

sessions = {
    "SES11": {"id":"SES11","name":"Spinning",     "day":"Monday / Wednesday / Friday","time":"Both",   "cost":900,  "instructors":["INS101","INS103"]},
    "SES12": {"id":"SES12","name":"Martial Arts",  "day":"Tuesday / Thursday",         "time":"Evening","cost":1100, "instructors":["INS102","INS104"]},
}

members = {
    "MEM1001": {"id":"MEM1001","first_name":"Andre",   "last_name":"Williams","contact":"876-310-4421","membership_type":"Platinum"},
    "MEM1002": {"id":"MEM1002","first_name":"Natasha", "last_name":"Clarke",  "contact":"876-422-8837","membership_type":"Diamond"},
    "MEM1003": {"id":"MEM1003","first_name":"Ricardo", "last_name":"Brown",   "contact":"876-551-6612","membership_type":"Gold"},
    "MEM1004": {"id":"MEM1004","first_name":"Simone",  "last_name":"Campbell","contact":"876-673-9903","membership_type":"Standard"},
    "MEM1005": {"id":"MEM1005","first_name":"Tyrone",  "last_name":"Reid",    "contact":"876-784-2251","membership_type":"Gold"},
    "MEM1006": {"id":"MEM1006","first_name":"Dionne",  "last_name":"Thompson","contact":"876-895-5570","membership_type":"Platinum"},
    "MEM1007": {"id":"MEM1007","first_name":"Kevon",   "last_name":"Grant",   "contact":"876-912-3398","membership_type":"Diamond"},
    "MEM1008": {"id":"MEM1008","first_name":"Latoya",  "last_name":"Morgan",  "contact":"876-334-7760","membership_type":"Standard"},
    "MEM1009": {"id":"MEM1009","first_name":"Fitzroy", "last_name":"Anderson","contact":"876-445-8812","membership_type":"Gold"},
    "MEM1010": {"id":"MEM1010","first_name":"Shanique","last_name":"Powell",  "contact":"876-556-0034","membership_type":"Standard"},
}

# LIST: check-in records
checkins = [
    {"member_id":"MEM1001","datetime":"2025-03-01 08:15:00"},
    {"member_id":"MEM1002","datetime":"2025-03-01 09:00:00"},
    {"member_id":"MEM1003","datetime":"2025-03-02 17:30:00"},
    {"member_id":"MEM1004","datetime":"2025-03-03 06:45:00"},
    {"member_id":"MEM1006","datetime":"2025-03-04 08:00:00"},
]

# LIST: session registrations
registrations = [
    {"member_id":"MEM1001","session_id":"SES11","date":"2025-03-01"},
    {"member_id":"MEM1001","session_id":"SES12","date":"2025-03-01"},
    {"member_id":"MEM1002","session_id":"SES12","date":"2025-03-01"},
    {"member_id":"MEM1003","session_id":"SES11","date":"2025-03-02"},
    {"member_id":"MEM1005","session_id":"SES11","date":"2025-03-03"},
    {"member_id":"MEM1006","session_id":"SES11","date":"2025-03-04"},
    {"member_id":"MEM1006","session_id":"SES12","date":"2025-03-04"},
    {"member_id":"MEM1007","session_id":"SES12","date":"2025-03-05"},
    {"member_id":"MEM1009","session_id":"SES11","date":"2025-03-08"},
]

# TUPLE: membership types (immutable)
MEMBERSHIP_TYPES = ("Platinum", "Diamond", "Gold", "Standard")

# DICTIONARY: membership costs and perks
MEMBERSHIP_INFO = {
    "Platinum": {"cost":10000, "free_sessions":4, "discount":0.15, "description":"4 free sessions + 15% discount"},
    "Diamond":  {"cost":7500,  "free_sessions":2, "discount":0.10, "description":"2 free sessions + 10% discount"},
    "Gold":     {"cost":4000,  "free_sessions":1, "discount":0.05, "description":"1 free session  +  5% discount"},
    "Standard": {"cost":2000,  "free_sessions":0, "discount":0.00, "description":"Basic gym access"},
}

# SET: valid time slots
VALID_TIME_SLOTS = {"Morning", "Evening", "Both"}

SYSTEM_PASSWORD  = "gym2025"
member_counter     = 1010
instructor_counter = 104
session_counter    = 12

# ── UTILITIES ─────────────────────────────────────────────────
def div(c="=", n=62): print(c * n)
def hdr(t): div(); print(f"  {t}"); div()
def pause(): input("\n  Press Enter to continue...")
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gen_mid():
    global member_counter
    member_counter += 1
    return f"MEM{member_counter}"

def gen_iid():
    global instructor_counter
    instructor_counter += 1
    return f"INS{instructor_counter}"

def gen_sid():
    global session_counter
    session_counter += 1
    return f"SES{session_counter}"

# ── LOGIN ─────────────────────────────────────────────────────
def login():
    """Authenticate user – max 3 attempts before shutdown."""
    div("*"); print("*" + "  GYM-ON-THE-ROCK BILLING SYSTEM  ".center(60) + "*"); div("*")
    attempts = 0
    while attempts < 3:
        pw = input(f"\n  Password ({3 - attempts} attempt(s) left): ")
        if pw == SYSTEM_PASSWORD:
            print("  Login successful!"); return
        attempts += 1
        if attempts < 3: print("  Wrong password, try again.")
        else: print("  Too many attempts. Shutting down."); exit()

# ── CHECK-IN ──────────────────────────────────────────────────
def checkin_member():
    """Record member visit and allow session registration."""
    hdr("CHECK-IN A MEMBER")
    mid = input("  Membership Number: ").strip().upper()
    if mid not in members:
        print("  Not found."); pause(); return
    m = members[mid]
    checkins.append({"member_id": mid, "datetime": now()})
    print(f"\n  Welcome {m['first_name']} {m['last_name']}! | Type: {m['membership_type']}")
    print("\n  Available Sessions:")
    for sid, s in sessions.items():
        print(f"  [{sid}] {s['name']:<18} {s['day']:<34} {s['time']:<8} ${s['cost']}")
    ans = input("\n  Register for a session? (yes/no): ").strip().lower()
    while ans == "yes":
        sid = input("  Session ID: ").strip().upper()
        if sid not in sessions:
            print("  Session not found.")
        elif any(r["member_id"]==mid and r["session_id"]==sid for r in registrations):
            print("  Already registered.")
        else:
            registrations.append({"member_id":mid,"session_id":sid,"date":datetime.date.today().strftime("%Y-%m-%d")})
            print(f"  Registered for {sessions[sid]['name']}!")
        ans = input("  Register for another? (yes/no): ").strip().lower()
    pause()

# ── ADD MEMBERS ───────────────────────────────────────────────
def add_members():
    """Add one or more members using a sentinel loop."""
    hdr("ADD MEMBER(S)")
    count = 0
    while True:
        fn = input("  First Name : ").strip().title()
        ln = input("  Last Name  : ").strip().title()
        ct = input("  Contact #  : ").strip()
        print("\n  Membership Types:")
        for i, t in enumerate(MEMBERSHIP_TYPES, 1):
            print(f"  {i}. {t:<10} ${MEMBERSHIP_INFO[t]['cost']:>6}/month  {MEMBERSHIP_INFO[t]['description']}")
        while True:
            ch = input("  Choice (1-4): ").strip()
            if ch in ("1","2","3","4"): break
            print("  Invalid. Enter 1-4.")
        mt  = MEMBERSHIP_TYPES[int(ch)-1]
        mid = gen_mid()
        members[mid] = {"id":mid,"first_name":fn,"last_name":ln,"contact":ct,"membership_type":mt}
        count += 1
        print(f"  Member added! ID: {mid}")
        if input("  Add another? (yes/no): ").strip().lower() != "yes": break
    print(f"  {count} member(s) added."); pause()

# ── ADD / UPDATE SESSION ──────────────────────────────────────
def add_update_session():
    """Add a new session or update an existing one."""
    hdr("ADD / UPDATE SESSION")
    print("  1. Add New Session\n  2. Update Existing Session")
    ch = input("  Choice (1/2): ").strip()

    if ch == "1":
        name = input("  Name    : ").strip().title()
        day  = input("  Day(s)  : ").strip().title()
        while True:
            t = input("  Time (Morning/Evening/Both): ").strip().title()
            if t in VALID_TIME_SLOTS: break
            print("  Invalid time slot.")
        while True:
            try:
                cost = float(input("  Cost ($): ").strip())
                if cost >= 0: break
                print("  Must be positive.")
            except ValueError: print("  Enter a number.")
        assigned = []
        if instructors:
            print("  Instructors:"); [print(f"  [{i}] {v['first_name']} {v['last_name']}") for i,v in instructors.items()]
            while True:
                iid = input("  Assign instructor ID (or done): ").strip().upper()
                if iid == "DONE": break
                if iid in instructors and iid not in assigned: assigned.append(iid); print("  Assigned.")
                elif iid in instructors: print("  Already assigned.")
                else: print("  Not found.")
        sid = gen_sid()
        sessions[sid] = {"id":sid,"name":name,"day":day,"time":t,"cost":cost,"instructors":assigned}
        print(f"  Session added! ID: {sid}")

    elif ch == "2":
        if not sessions: print("  No sessions found."); pause(); return
        [print(f"  [{k}] {v['name']}") for k,v in sessions.items()]
        sid = input("  Session ID to update: ").strip().upper()
        if sid not in sessions: print("  Not found."); pause(); return
        s = sessions[sid]
        v = input(f"  Name   [{s['name']}]: ").strip().title()
        if v: s["name"] = v
        v = input(f"  Day(s) [{s['day']}]: ").strip().title()
        if v: s["day"] = v
        v = input(f"  Time   [{s['time']}]: ").strip().title()
        if v in VALID_TIME_SLOTS: s["time"] = v
        v = input(f"  Cost   [${s['cost']}]: ").strip()
        if v:
            try: s["cost"] = float(v)
            except ValueError: print("  Invalid cost, kept original.")
        print(f"  Session {sid} updated.")
    else:
        print("  Invalid option.")
    pause()

# ── ADD INSTRUCTOR ────────────────────────────────────────────
def add_instructor():
    """Add one or more instructors using a sentinel loop."""
    hdr("ADD FACILITATOR / INSTRUCTOR")
    count = 0
    while True:
        fn = input("  First Name      : ").strip().title()
        ln = input("  Last Name       : ").strip().title()
        ct = input("  Contact #       : ").strip()
        sp = input("  Specialization  : ").strip().title()
        iid = gen_iid()
        instructors[iid] = {"id":iid,"first_name":fn,"last_name":ln,"contact":ct,"specialization":sp}
        count += 1
        print(f"  Instructor added! ID: {iid}")
        if input("  Add another? (yes/no): ").strip().lower() != "yes": break
    print(f"  {count} instructor(s) added."); pause()

# ── REPORTS ───────────────────────────────────────────────────
def report_all_members():
    """List all members."""
    hdr("REPORT: ALL MEMBERS")
    if not members: print("  No members."); pause(); return
    print(f"  {'ID':<10} {'First':<14} {'Last':<14} {'Contact':<14} {'Type'}")
    print("  " + "-"*62)
    for m in members.values():
        print(f"  {m['id']:<10} {m['first_name']:<14} {m['last_name']:<14} {m['contact']:<14} {m['membership_type']}")
    print(f"\n  Total: {len(members)} member(s)"); pause()

def report_sessions_schedule():
    """List all sessions with instructors."""
    hdr("REPORT: CLASS SCHEDULE")
    if not sessions: print("  No sessions."); pause(); return
    for s in sessions.values():
        names = [f"{instructors[i]['first_name']} {instructors[i]['last_name']}" for i in s["instructors"] if i in instructors]
        print(f"  [{s['id']}] {s['name']} | {s['day']} | {s['time']} | ${s['cost']}")
        print(f"       Instructors: {', '.join(names) if names else 'TBA'}\n")
    pause()

def report_members_by_type():
    """Group members by membership type with totals."""
    hdr("REPORT: MEMBERS BY TYPE")
    for t in MEMBERSHIP_TYPES:
        grp  = [m for m in members.values() if m["membership_type"] == t]
        cost = MEMBERSHIP_INFO[t]["cost"]
        print(f"\n  -- {t} (${cost:,}/month) --")
        if grp:
            for m in grp: print(f"  {m['id']}  {m['first_name']} {m['last_name']}")
            print(f"  Count: {len(grp)}  |  Total Fees: ${len(grp)*cost:,.2f}")
        else: print("  No members.")
    pause()

def report_session_registrations():
    """List registrations and earnings per session."""
    hdr("REPORT: SESSION REGISTRATIONS")
    if not sessions: print("  No sessions."); pause(); return
    for sid, s in sessions.items():
        regs = [r for r in registrations if r["session_id"] == sid]
        print(f"\n  [{sid}] {s['name']} – ${s['cost']}/class")
        if regs:
            for r in regs:
                m = members.get(r["member_id"])
                name = f"{m['first_name']} {m['last_name']}" if m else "Unknown"
                print(f"  {r['member_id']}  {name:<26} {r['date']}")
            print(f"  Registered: {len(regs)}  |  Earned: ${len(regs)*s['cost']:,.2f}")
        else: print("  No registrations.")
    pause()

def report_member_monthly_bill():
    """Calculate and display each member's monthly bill with discounts."""
    hdr("REPORT: MONTHLY BILLING")
    if not members: print("  No members."); pause(); return
    print(f"  {'ID':<10} {'Name':<24} {'Type':<10} {'Gym Fee':>9} {'Sess Fee':>10} {'Total':>9}")
    print("  " + "-"*76)
    grand = 0
    for mid, m in members.items():
        t    = m["membership_type"]
        fee  = MEMBERSHIP_INFO[t]["cost"]
        disc = MEMBERSHIP_INFO[t]["discount"]
        regs = [r for r in registrations if r["member_id"] == mid]
        sfee = sum(sessions[r["session_id"]]["cost"] * (1 - disc) for r in regs if r["session_id"] in sessions)
        snames = [sessions[r["session_id"]]["name"] for r in regs if r["session_id"] in sessions]
        total = fee + sfee; grand += total
        print(f"  {mid:<10} {m['first_name']+' '+m['last_name']:<24} {t:<10} ${fee:>8,.2f} ${sfee:>9,.2f} ${total:>8,.2f}")
        print(f"  {'':10} Sessions: {', '.join(snames) if snames else 'None'}")
    print("  " + "-"*76)
    print(f"  {'GRAND TOTAL':>58} ${grand:>8,.2f}"); pause()

def print_report():
    """Report sub-menu."""
    options = {
        "1":("All Members",           report_all_members),
        "2":("Class Schedule",         report_sessions_schedule),
        "3":("Members by Type",        report_members_by_type),
        "4":("Session Registrations",  report_session_registrations),
        "5":("Monthly Billing",        report_member_monthly_bill),
    }
    while True:
        hdr("PRINT REPORT")
        for k,(label,_) in options.items(): print(f"  {k}. {label}")
        print("  6. Back")
        ch = input("  Choice: ").strip()
        if ch == "6": break
        elif ch in options: options[ch][1]()
        else: print("  Invalid option.")

# ── MAIN MENU ─────────────────────────────────────────────────
def main_menu():
    """Main menu – loops until user exits (sentinel = 6)."""
    while True:
        div(); print("=" + "  GYM-ON-THE-ROCK BILLING SYSTEM  ".center(60) + "="); div()
        print("  1. Check-in Member\n  2. Add Member(s)\n  3. Add / Update Session")
        print("  4. Add Instructor\n  5. Print Report\n  6. Exit")
        div("-")
        ch = input("  Choice (1-6): ").strip()
        if   ch == "1": checkin_member()
        elif ch == "2": add_members()
        elif ch == "3": add_update_session()
        elif ch == "4": add_instructor()
        elif ch == "5": print_report()
        elif ch == "6": print("  Goodbye!"); div(); break
        else: print("  Invalid option.")

# ── ENTRY POINT ───────────────────────────────────────────────
if __name__ == "__main__":
    login()
    main_menu()